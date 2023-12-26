import luigi


class GetDataTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget('hello-luigi.txt')

    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Hello Luigi!")

