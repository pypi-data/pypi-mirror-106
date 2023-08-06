import json
import io
import csv
import typing


class Results:
    def __init__(self):
        self._dict = {}
        self._max_metric_size = None
        self._results_keys = None
        self._repo_size = {}

    def add(self, repository: str, values: typing.Dict[str, typing.Any]):
        self._dict[repository] = values
        self._repo_size[repository] = max([len(str(v)) for v in
                                           list(values.values()) + [
                                               repository]])
        if not self._max_metric_size:
            self._results_keys = list(values.keys())
            self._max_metric_size = max(len(r) for r in self._results_keys)

    def _print_line(self, output):
        print("+" + "-" * (self._max_metric_size + 2) + "+", end="",
              file=output)
        for repository in self._dict:
            print(f"-{'-' * self._repo_size[repository]}-+", end="",
                  file=output)
        print(file=output)

    def string(self):
        output = io.StringIO()
        if not self._dict:
            return ""
        self._print_line(output)
        top_right = f"| %{self._max_metric_size}s |" % "metric"
        print(top_right, end="", file=output)
        for repository in self._dict:
            print(f" %{self._repo_size[repository]}s |" % repository, end="",
                  file=output)
        print(file=output)
        self._print_line(output)
        for name in self._results_keys:
            print(f'| %{self._max_metric_size}s |' % name, end="", file=output)
            for repository in self._dict:
                print(f" %{self._repo_size[repository]}s |" %
                      self._dict[repository][name], end="", file=output)
            print(file=output)
        self._print_line(output)
        return output.getvalue()

    def csv(self):
        output = io.StringIO()
        csv_writer = csv.writer(output, lineterminator="\n")
        csv_writer.writerow(["metric"] + list(self._dict.keys()))
        for metric in self._results_keys:
            values = [self._dict[repository][metric]
                      for repository in self._dict]
            csv_writer.writerow([metric] + values)
        return output.getvalue()

    def json(self):
        return json.dumps(self._dict,  indent=4, sort_keys=True)
