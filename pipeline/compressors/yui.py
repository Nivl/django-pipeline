from pipeline.conf import settings
from pipeline.compressors import SubProcessCompressor


class YUICompressor(SubProcessCompressor):
    def compress_common(self, content, type_, arguments):
        command = '%s --type=%s %s' % (settings.PIPELINE_YUI_BINARY, type_, arguments)
        return self.execute_command(command, content)

    def compress_js(self, js):
        return self.compress_common(js, 'js', settings.PIPELINE_YUI_JS_ARGUMENTS)

    def compress_css(self, css):
        return self.compress_common(css, 'css', settings.PIPELINE_YUI_CSS_ARGUMENTS)
