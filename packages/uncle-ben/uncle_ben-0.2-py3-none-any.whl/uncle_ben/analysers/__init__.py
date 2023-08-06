import sys
import inspect

from uncle_ben.analysers.radon import RawAnalyser, McCabeAnalyser, MaintainabilityAnalyser, HalsteadAnalyser # noqa
from uncle_ben.analysers.git import GitAnalyser # noqa
from uncle_ben.analysers.ci import BitbucketCIAnalyser, GitlabCIAnalyser # noqa
from uncle_ben.analysers.package_usage import PackageUsageAnalyser # noqa
from uncle_ben.analysers.pylama import PyLamaAnalyser # noqa

analysers = []
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        analysers.append(obj)
