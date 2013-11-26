import sublime, sublime_plugin, os
from subprocess import Popen

class OpenProjectDirectory(sublime_plugin.TextCommand):

  settings = sublime.load_settings('OpenProjectDirectory.sublime-settings')
  path = ""
  dirs = []

  def run(self, edit):
    self.path = self.settings.get("project_root") or "/Users/nucc/Works"
    self.dirs = [ filename for filename in os.listdir(self.path) if os.path.isdir( os.path.join(self.path, filename) ) ]
    sublime.active_window().show_quick_panel(self.dirs, self.valueIsSelected)

  def valueIsSelected(self, value):
    if value == -1:
      return

    self.selected_directory = os.path.join(self.path, self.dirs[value])
    self.sublime_command_line([self.selected_directory])

  def get_sublime_path(self):
    if sublime.platform() == 'osx':
        return '/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl'
    elif sublime.platform() == 'linux':
        return open('/proc/self/cmdline').read().split(chr(0))[0]
    else:
        return sys.executable

  def sublime_command_line(self, args):
    args.insert(0, self.get_sublime_path())
    return Popen(args)
