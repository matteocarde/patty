import os
import shutil

DOMAINS = 20


def main():
    path = "instances"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    for i in range(3, DOMAINS + 1):
        rows = ["r{:02d}".format(j) for j in range(1, i + 1)]
        columns = ["c{:02d}".format(j) for j in range(1, i + 1)]

        problem = f'''(define (problem pb{i})
            (:domain grid)
            (:objects 
                {" ".join([f'{r}' for r in rows])} - row
                {" ".join([f'{c}' for c in columns])} - column
                r - robot
            )
            (:init
                {" ".join([f'(isLeft {a} {b})' for (a, b) in zip(columns, columns[1:] + [columns[0]])])}
                {" ".join([f'(isDown {a} {b})' for (a, b) in zip(rows, rows[1:] + [rows[0]])])}
                (atColumn r {columns[0]})
                (atRow r {rows[0]})
            )
            (:goal
                (and  
                    (atColumn r {columns[len(columns) // 2]})
                    (atRow r {rows[len(rows) // 2]})
                )
            )
            )

                    '''
        with open(f"{path}/problem-{i}.pddl", "w") as f:
            f.write(problem)


if __name__ == '__main__':
    main()
