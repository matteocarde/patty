import time

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
        client = boto3.client('logs')
        cmd = client.get_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=name,
            limit=10000,
        )
        return cmd["events"]

    @staticmethod
    def saveLogs(exp, file):
        events = ['"' + e["message"] + '"' for e in CloudLogger.read(exp)]
        with open(file, "w") as f:
            f.write("\n".join(sorted(events)))
