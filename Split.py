import os
import sublime, sublime_plugin
class SplitCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.window = self.view.window()
        self.root = os.path.split(self.view.file_name())[0]
        self.sels = self.view.sel()
        self.text = self.view.substr(self.sels[0])
        self.syntax = self.view.settings().get('syntax')
        self.show_name_input()

    def show_name_input(self): 
        self.window.show_input_panel(
            'File Name', "",
            self.entered_input, self.update_input, None
        )

    def entered_input(self, filename):
        file_path = os.path.join(self.root, filename)
        if not os.path.exists(self.root):
            os.mkdir(self.root)        
        with open(file_path, 'w+') as f:
            f.write(self.text)
        edit = self.view.begin_edit()
        self.view.replace(edit, self.sels[0], "Splited To: " + file_path)
        self.view.end_edit(edit)
        self.view.run_command('toggle_comment')
        view = self.window.open_file(file_path)   
        view.set_syntax_file(self.syntax)
    def update_input():
        pass









