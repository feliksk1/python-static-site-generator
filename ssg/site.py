import Path from pathlib

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
        
    def create_dir(self, path):
        directory = Path(self.dest + '/' + Path.relativeTo(self.source))
        directory.mkdir(directory, parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        
        for path in self.source.rglob(*):
            if path.directory
                create_dir(self, path)