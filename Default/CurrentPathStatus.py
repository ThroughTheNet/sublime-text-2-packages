import sublime, sublime_plugin

fn = lambda fn: fn or 'untitled'

class ShowBufferPath(sublime_plugin.WindowCommand):
    """Display path in status bar.
    """
    def run(self):
        view = self.window.active_view()
        #view.set_status('Path', fn(view.file_name()))
        sublime.status_message(fn(view.file_name()))


class ShowBufferPathOnFocus(sublime_plugin.EventListener)::
    """Display path in status bar when view gets focus.
    """
    def on_activated(self, view):
        #view.set_status('Path', fn(view.file_name()))
        sublime.status_message(fn(view.file_name()))