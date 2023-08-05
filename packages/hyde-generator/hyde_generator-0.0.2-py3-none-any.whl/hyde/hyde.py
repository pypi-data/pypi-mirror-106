from argparse import ArgumentParser
from os import chdir, getcwd, listdir, mkdir, remove, system
from os.path import isdir, isfile, join
from shutil import copy, copytree, rmtree

from jinja2 import Environment, FileSystemLoader
from markdown import Markdown
from yaml import safe_load

class BuildFile:
    def __init__(self) -> None:
        self.environment = Environment(
            loader = FileSystemLoader(
                join(
                    getcwd(),
                    "layouts"
                )
            )
        )
        self.markdown = Markdown()

    def loadALlConfiguration(self) -> tuple:
        with open("data/navigation.yml") as navigation:
            navigation = safe_load(navigation)
        with open("data/pages.yml") as pages:
            pages = safe_load(pages)
        return (
            navigation,
            pages
        )

    def fillTemplate(self, title: str, navigation: dict, main: str) -> str:
        renderedNavigation = [
            f"<a href = \"{navigation[name]}\">{name}</a>"
            for name in navigation
        ]
        renderedNavigation = "\n".join(renderedNavigation)
        with open("data/keywords.yml") as keywords:
            keywords = safe_load(keywords)
            keywords = ",".join(keywords)
        return f"""
        {{% extends "default.html" %}}
        {{% block keywords %}}
            <meta name = \"keywords\" content = \"{keywords}\">
        {{% endblock %}}
        {{% block title %}}
            {title} | Aarush Gupta
        {{% endblock %}}
        {{% block navigation %}}
            {renderedNavigation}
        {{% endblock %}}
        {{% block main %}}
            {main}
        {{% endblock %}}
        """

    def __main__(self, filename: str) -> None:
        navigation, pages = self.loadALlConfiguration()
        with open(f"pages/{filename}") as fileControl:
            fileContent = fileControl.read()
        mainHTML = self.markdown.convert(fileContent)
        try:
            filled = self.fillTemplate(pages[filename], navigation, mainHTML)
        except KeyError:
            print(f"[ERROR] no title found for \"{filename}\" in \"data/pages.yml\"")
            exit()
        compliledTemplate = self.environment.from_string(filled)
        compliledTemplate = compliledTemplate.render()
        publicHTMLFilename = filename.split(".")[0] + ".html"
        try:
            with open(f"public/{publicHTMLFilename}", "w+") as publicHTML:
                publicHTML.write(compliledTemplate)
        except FileNotFoundError:
            mkdir("public")
            self.__main__(filename)
        print(f"[INFO] Built \"pages/{filename}\" as \"public/{publicHTMLFilename}\"")

def retrieveCommands() -> tuple:
    parser = ArgumentParser(
        prog = "hyde",
        description = "a simple static site generator"
    )
    parser.add_argument("build", help = "initate build sequence for all markdown files in the \"pages\" directory", nargs = "?")
    parser.add_argument("serve", help = "serve compiled html files", nargs = "?")
    arguments = parser.parse_args()
    return arguments.build

def discoverMarkdownFiles() -> list:
    markdownFiles = []
    sourceDirectory = join(
        getcwd(),
        "pages"
    )
    markdownFiles = [item for item in listdir(sourceDirectory)]
    return markdownFiles

def clearPublicDirectory() -> None:
    public = join(
        getcwd(),
        "public"
    )
    if isdir(public):
        for item in listdir(public):
            itemPath = join(
                public,
                item
            )
            if item != ".git":
                if isdir(itemPath):
                    rmtree(itemPath)
                else:
                    remove(itemPath)
                print(f"[INFO] Deleted public/{item}")

def copyAssets() -> None:
    copytree(
        join(
            getcwd(),
            "assets"
        ),
        join(
            getcwd(),
            "public",
            "assets"
        )
    )
    print("[INFO] Moved \"assets/\" to \"public/assets/\"")

def copyExtras() -> None:
    extrasPath = join(
        getcwd(),
        "extras"
    )
    for extra in listdir(extrasPath):
        source = join(
            getcwd(),
            "extras",
            extra
        )
        destination = join(
            getcwd(),
            "public",
            extra
        )
        copy(source, destination)
        print(f"[INFO] Moved \"extras/{extra}\" to \"public/{extra}\"")

def main() -> None:
    command = retrieveCommands()
    if command == "build":
        clearPublicDirectory()
        for markdown in discoverMarkdownFiles():
            buildFile = BuildFile()
            buildFile.__main__(markdown)
        copyExtras()
        copyAssets()
        exit()
    if command == "serve":
        chdir(
            join(
                getcwd(),
                "public"
            )
        )
        print("[INFO] Starting HTTP server to serve files")
        system("python3 -m http.server")
        exit()
    print("This is hyde - a simple static site generator")
    print("Run \"hyde --help\" to get started")