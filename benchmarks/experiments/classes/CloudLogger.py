import time
from datetime import datetime
from typing import List

import boto3

LOG_GROUP = "patty"
ERROR_STREAM = "errors"


class CloudLogger:

    def __init__(self, experiment):
        self.client = boto3.client('logs')
        self.streamName = experiment
        self.errorStreamName = f"{experiment}-{ERROR_STREAM}"

        self.__createStream(self.streamName)
        self.__createStream(self.errorStreamName)

    def log(self, message):
        self.client.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=self.streamName,
            logEvents=[{'timestamp': round(time.time() * 1000), 'message': str(message)}]
        )

    def error(self, error):
        self.client.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=self.errorStreamName,
            logEvents=[{'timestamp': round(time.time() * 1000), 'message': str(error)}]
        )

    def __createStream(self, name):
        streams = self.client.describe_log_streams(
            logGroupName=LOG_GROUP,
            logStreamNamePrefix=name
        )

        if not streams["logStreams"]:
            self.client.create_log_stream(
                logGroupName=LOG_GROUP,
                logStreamName=name
            )

    @staticmethod
    def read(name):
        events = list()
        client = boto3.client('logs')
        startTime = round(time.time() * 1000) - 1000 * 60 * 60 * 24 * 30 * 12
        endTime = round(time.time() * 1000)
        nextToken = None
        while True:
            args = {
                "startTime": startTime,
                "endTime": endTime,
                "logGroupName": LOG_GROUP,
                "logStreamName": name,
                "startFromHead": True,
                "limit": 10000,
            }
            if nextToken:
                args["nextToken"] = nextToken
            try:
                cmd = client.get_log_events(**args)
            except Exception as e:
                print("Error:", args)
                raise e
            nextToken = cmd["nextForwardToken"]
            print(f"Saved {len(cmd['events'])} instances from {datetime.fromtimestamp(startTime / 1000)} "
                  f"to {datetime.fromtimestamp(endTime / 1000)}")
            events += cmd["events"]
            if not cmd["events"]:
                break

        print(f"Total Received: {len(events)} instances")
        return events

    @staticmethod
    def saveLogs(exp, file):
        events = ['"' + e["message"] + '"' for e in CloudLogger.read(exp)]
        with open(file, "w") as f:
            f.write("\n".join(sorted(events)))

    @staticmethod
    def appendLogs(exp, file, keepSolvers: List[str]):
        events = ['"' + e["message"] + '"' for e in CloudLogger.read(exp)]
        keepEvents = []
        for e in events:
            for s in keepSolvers:
                if f"{s}," in e:
                    keepEvents.append(e)
                    break
        with open(file, "a") as f:
            f.write("\n")
            f.write("\n".join(sorted(keepEvents)))
