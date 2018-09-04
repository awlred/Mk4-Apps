"""Official TiLDA MK4 Badge Store App

switches between app libraries, updates and installs apps.

To publish apps use https://badge.emfcamp.org"""

___license___      = "MIT"
___title___        = "Badge Store"
___dependencies___ = ["badge_store", "dialogs", "ugfx_helper", "app", "database", "ospath"]
___categories___   = ["System"]
___bootstrapped___ = True

import ugfx_helper, os, database, wifi, app, ospath
from dialogs import *
from lib.badge_store import BadgeStore
from app import *

### VIEWS ###

ugfx_helper.init()

url = database.get("badge_store.url", "http://badgeserver.emfcamp.org/2018")
repo = database.get("badge_store.repo", "emfcamp/Mk4-Apps")
ref = database.get("badge_store.ref", "master")
store = BadgeStore(url=url, repo=repo, ref=ref)
title = "TiLDA Badge Store"

def clear():
    ugfx.clear()

def show_categories():
    clear()
    with WaitingMessage(title=title, text="Loading categories..."):
        menu_items = [{"title": c, "category": c} for c in store.get_categories()]

    option = prompt_option(menu_items, none_text="Back", title="Install: Categories")

    if option:
        show_apps(option["category"])
    else:
        return

def show_apps(c):
    clear()
    menu_items = [{"title": a, "app": a} for a in store.get_apps(c)]

    option = prompt_option(menu_items, none_text="Back", title="Install: " + c)

    if option:
        show_app(option["app"],c)
    else:
        return

def show_app(a,c):
    clear()
    with WaitingMessage(title=title, text="Loading app description..."):
        app_info = store.get_app(a)

    app_text = "App:\n"
    try:
        app_text += app_info["title"] + '\n'
    except:
        pass
    finally:
        app_text += a + '\n\nDescription:\n' + app_info["description"].strip()
    install = prompt_boolean(app_text , title="Install App", true_text="Install", false_text="Back")

    if install:
        app_text = "App:\n"
        try:
            app_text += app_info["title"] + '\n'
        except:
            pass
        finally:
            app_text += a + '\n\n'

        with WaitingMessage(title="Installing App...", text="%sGetting ready..." % app_text) as message:
            installers = store.install(_get_current_apps() + [a])
            n = len(installers)
            for i, installer in enumerate(installers):
                message.text = "%s%s (%s/%s)" % (app_text + "Downloading files...\n\n", installer.path, i + 1, n)
                installer.download()
            app.uncache_apps()

        launch = prompt_boolean(
            "%sSuccessfully installed.\n\nPress A to launch the app.\n\nPress B to list more \"%s\" apps." % (app_text, c), title="Install Success!", true_text="Launch", false_text="Back")
        if (launch):
            for app_obj in get_apps():
                if app_obj.name == a:
                    app_obj.boot()
        else:
            show_apps(c)



def show_update():
    clear()
    update = prompt_boolean("Do you want to update all apps on this badge?", title="Update", true_text="OK", false_text="Back")
    if update:
        clear()
        with WaitingMessage(title=title, text="Please wait...") as message:
            installers = store.install(_get_current_apps())
            n = len(installers)
            for i, installer in enumerate(installers):
                message.text = "%s (%s/%s)" % (installer.path, i + 1, n)
                installer.download()
        notice("Your badge has been successfully updated", title=title, close_text="Back")

def show_remove():
    clear()
    app_to_remove = prompt_option(_get_current_apps(), none_text="Back", text="Select App to remove")
    if app_to_remove:
        ospath.recursive_rmdir(app_to_remove)
        app.uncache_apps()
        notice("%s has been removed" % app_to_remove, title=title, close_text="Back")

def main_menu():
    while True:
        clear()

        menu_items = [
            {"title": "Install Apps", "function": show_categories},
            {"title": "Update all Apps", "function": show_update},
            {"title": "Remove App", "function": show_remove}
        ]

        option = prompt_option(menu_items, none_text="Exit", text="What do you want to do?", title=title)

        if option:
            option["function"]()
        else:
            break

def _get_current_apps():
    return [a.name for a in app.get_apps()]

wifi.connect(show_wait_message=True)
main_menu()
app.restart_to_default()
