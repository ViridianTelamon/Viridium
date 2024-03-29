"""
    Copyright (C) 2024 ViridianTelamon (Viridian)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtNetwork
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtCore import QUrl
from PyQt5.QtPrintSupport import *
from configparser import ConfigParser
import socket
import sys
import os

print("Viridium")

print("\nBy:  ViridianTelamon.")

#Use The Search Bar To Search The Web With A Certain Search Engine.

#Use Control And Your Mouse Scroller Together To Zoom In And Out Of A Web Page.

#Use The Control Button And Tab Together To Go Through All The Tabs That You Have Opened.

#Use The Shortcuts To Buttons In The Browser These Are All Shortcuts In The Web Browser.

HOMEPAGE = "https://search.brave.com"

SEARCH = "https://search.brave.com/search?q="

THEME = "Light"

PROXY_IP = "127.0.0.1"

PROXY_PORT = "3000"

#Main window.
class MainWindow(QMainWindow):
    #Constructor.
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(HOMEPAGE))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QtGui.QIcon("Logo.png"))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.showMaximized()
                     
        #Setting the user agent of the browser.
        chrome = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        edge = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.0 Safari/537.36 Edg/92.0.874.0"
        firefox = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
        brave = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 Safari/537.36 Brave/75"
        safari = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15"
        chromium = "Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/88.0.4324.150 Chrome/88.0.4324.150 Safari/537.36 Tesla/DEV-BUILD-4d1a3f465b3a"
        viridium = "Viridium"

        user_agent_string = chrome

        self.browser.page().profile().setHttpUserAgent(user_agent_string)

        #Homepage.
        self.configuration = ConfigParser()
        
        self.homepage = HOMEPAGE

        self.search_engine_choice = SEARCH

        #Settings.
        self.websettings = QWebEngineSettings.globalSettings()
        self.websettings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.websettings.setAttribute(QWebEngineSettings.PluginsEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.WebRTCPublicInterfacesOnly, True)
        self.websettings.setAttribute(QWebEngineSettings.AllowGeolocationOnInsecureOrigins, False)
        self.websettings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, False)
        self.websettings.setAttribute(QWebEngineSettings.LocalStorageEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.websettings.setAttribute(QWebEngineSettings.HyperlinkAuditingEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.ScreenCaptureEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.TouchIconsEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.websettings.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)
        self.websettings.setAttribute(QWebEngineSettings.ScrollAnimatorEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.XSSAuditingEnabled, True)
        self.websettings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
        self.websettings.setAttribute(QWebEngineSettings.SpatialNavigationEnabled, False)
        self.websettings.setAttribute(QWebEngineSettings.PdfViewerEnabled, True)

        self.settings_window()

        self.cancel_settings()

        #Creating a tab widget.
        self.tabs = QTabWidget()

        #Making the tabs movable.
        self.tabs.setMovable(True)
 
        #Making document mode true.
        self.tabs.setDocumentMode(True)
 
        #Adding action when tab is changed.
        self.tabs.currentChanged.connect(self.current_tab_changed)
 
        #Making tabs closeable.
        self.tabs.setTabsClosable(True)
 
        #Adding action when tab close is requested.
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
 
        #Making tabs as central widget.
        self.setCentralWidget(self.tabs)
 
        #Creating a tool bar for navigation.
        navtb = QToolBar("Navigation")
        #Making it not movable.
        navtb.setMovable(False)
        #Making it so you can not delete it.
        navtb.setFloatable(False)
 
        #Adding tool bar tot he main window.
        self.addToolBar(navtb)
 
        #Creating back action.
        back_button = QAction("Go Back To Previous Page", self)
        back_button.setIcon(QtGui.QIcon("BackArrow.svg"))
        #Adding action to back button.
        back_button.triggered.connect(lambda: self.tabs.currentWidget().back())
        #Setting the short cut for it.
        back_button.setShortcut("Ctrl+Z")
        #Adding this to the navigation tool bar.
        navtb.addAction(back_button)
 
        #Similarly adding forward button.
        next_button = QAction("Go Forward To Next Page", self)
        next_button.setIcon(QtGui.QIcon("ForwardArrow.svg"))
        next_button.triggered.connect(lambda: self.tabs.currentWidget().forward())
        next_button.setShortcut("Ctrl+Y")
        navtb.addAction(next_button)
 
        #Similarly adding reload button.
        reload_button = QAction("Refresh The Page", self)
        reload_button.setIcon(QtGui.QIcon("RefreshPage.svg"))
        reload_button.triggered.connect(lambda: self.tabs.currentWidget().reload())
        reload_button.setShortcut("Ctrl+R")
        navtb.addAction(reload_button)
 
        #Creating home action.
        home_button = QAction("Go To The Home Page", self)
        home_button.setIcon(QtGui.QIcon("HomePage.svg"))
 
        #Adding action to home button.
        home_button.triggered.connect(self.navigate_home)
        home_button.setShortcut("Ctrl+H")
        navtb.addAction(home_button)

        #Adding a separator.
        navtb.addSeparator()

        #Adding another separator.
        navtb.addSeparator()

        #Similarly adding add new tab action.
        add_tab_button = QAction("Add New Tab", self)
        add_tab_button.setIcon(QtGui.QIcon("AddTab.svg"))
        add_tab_button.triggered.connect(self.add_new_tab)
        add_tab_button.setShortcut("Ctrl+T")
        navtb.addAction(add_tab_button)
        
        #Adding another separator.
        navtb.addSeparator()

        #Adding another separator.
        navtb.addSeparator()

        #Similarly adding lock and unlock https and http action.
        self.ssl_icon = QLabel("SSL Check")
        self.ssl_icon.setPixmap(QPixmap("Locked.svg"))
        navtb.addWidget(self.ssl_icon)

        #Creating a line edit widget for URL.
        self.urlbar = QLineEdit()
        #Adding action to line edit when enter key is pressed.
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        #Adding line edit to tool bar.
        navtb.addWidget(self.urlbar)
        #Text for the URL bar.
        self.urlbar.setPlaceholderText("https://")
              
        #Creating the search bar.
        self.search_bar = QLineEdit()
        #Adding the search bar to the main tool bar.
        navtb.addWidget(self.search_bar)
        #Adding the action to the search bar.
        self.search_bar.returnPressed.connect(self.search_bar_navigation)
        #Making the search bar's size not to big and not to small.
        #self.search_bar.setFixedWidth(400)
        self.search_bar.setFixedWidth(400)
        #Search bar text.
        self.search_bar.setPlaceholderText("Search")
        #Search bar icon.
        self.search_icon = QLabel("Search Icon", self.search_bar)
        self.search_icon.setPixmap(QPixmap("Search.svg"))

        #Similarly adding stop action.
        stop_button = QAction("Stop Loading The Current Page", self)
        stop_button.setIcon(QtGui.QIcon("StopPage.svg"))
        stop_button.triggered.connect(lambda: self.tabs.currentWidget().stop())
        stop_button.setShortcut("Ctrl+K")
        navtb.addAction(stop_button)

        #Similarly adding open file action.
        file_button = QAction("Open A Local File From Your Computer", self)
        file_button.setIcon(QtGui.QIcon("FileOpen.svg"))
        file_button.triggered.connect(self.open_file)
        file_button.setShortcut("Ctrl+F")
        navtb.addAction(file_button)

        #Similarly adding screenshot action.
        #screenshot_button = QAction("Screenshot This Page", self)
        #screenshot_button.setIcon(QtGui.QIcon("Camera.svg"))
        #screenshot_button.triggered.connect(self.screenshot_page)
        #navtb.addAction(screenshot_button)

        #Similarly adding settings action.
        settings_button = QAction("Settings Menu", self)
        settings_button.setIcon(QtGui.QIcon("Settings.svg"))
        settings_button.triggered.connect(self.settings_window)
        settings_button.setShortcut("Ctrl+B")
        navtb.addAction(settings_button)

        #Creating first tab.
        self.add_new_tab(QUrl(self.homepage), "Homepage")
 
        #Showing all the components.
        self.show()
 
        #Setting window title.
        self.setWindowTitle("Viridium |  By:  ViridianTelamon")
    
    #The method for making the search bar work.
    def search_bar_navigation(self, qurl = None, label = "Blank"):
        #Getting the text of the search bar.
        search_bar_text = self.search_bar.text()
        self.search_bar_url = self.search_engine_choice + search_bar_text

        #Accessing the web browsers URL.
        qurl = QUrl(self.search_bar_url)
        browser = QWebEngineView()

        #Changing the website.
        self.tabs.currentWidget().setUrl(QUrl(self.search_bar_url))

        #Setting url to browser.
        browser.setUrl(QUrl(self.search_bar_url))

        self.search_bar.setText("")

    #Method for adding new tab.
    def add_new_tab(self, qurl = None, label ="Blank"):
        #If url is blank.
        if qurl is None:
            #Creating a url to be the default one.
            qurl = QUrl(self.homepage)
 
        #Creating a QWebEngineView object.
        browser = QWebEngineView()
 
        #Setting url to browser.
        browser.setUrl(QUrl(self.homepage))
 
        #Setting tab index.
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        #Update the url
        browser.urlChanged.connect(lambda qurl, browser = browser:
                                   self.update_urlbar(qurl, browser))

        #Set the tab title.
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                     self.tabs.setTabText(i, browser.page().title()))

        #Update the tab's icon.
        self.tabs.setTabIcon(i, browser.icon())
        browser.iconChanged.connect(lambda icon, browser=browser: self.update_icon(browser, icon))

        #Making the page more readable while having a closer up view of it.
        #browser.setZoomFactor(1.5)

    #Update the tab's icon for the certain website that it's on.
    def update_icon(self, browser, icon):
        index = self.tabs.indexOf(browser)
        self.tabs.setTabIcon(index, icon)
 
    #When button is clicked clicked on tabs button.
    def tab_open(self, i):
        #Checking index.
        if i == -1:
            #Creating a new tab.
            self.add_new_tab()

    #When tab is changed.
    def current_tab_changed(self, i):
        #Get the current url.
        qurl = self.tabs.currentWidget().url()
 
        #Update that url.
        self.update_urlbar(qurl, self.tabs.currentWidget())
 
        #Update that title.
        self.update_title(self.tabs.currentWidget())

    #If the tab is closed.
    def close_current_tab(self, i):
        #If there is only one tab as well.
        if self.tabs.count() < 2:
            #Do nothing.
            return
        page = self.tabs.widget(i)
        self.tabs.removeTab(i)
        page.deleteLater()
 
    #Method for updating the title.
    def update_title(self, browser):
        #If signal is not from the current tab.
        if browser != self.tabs.currentWidget():
            #Then do nothing.
            return

        #Set the window title.
        self.setWindowTitle("Viridium |  By:  ViridianTelamon")
 
    #Action to go to home.
    def navigate_home(self):
        #Go to home page.
        self.tabs.currentWidget().setUrl(QUrl(self.homepage))
 
    #Method for navigate to url.
    def navigate_to_url(self):
        #Gets the line edit text and converts it into a QUrl object.
        q = QUrl(self.urlbar.text())

        #Clears all cookies from the web browser before accessing a new web page.
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
 
        #If the scheme is blank.
        if q.scheme() == "":
            #Set a scheme.
            qurl = (self.tabs.currentWidget()).url()
            q.setScheme("https")
            q.path()

        #Change the SSL Check icon if the website is encrypted or not.
        if q.scheme() == "https":
            self.ssl_icon.setPixmap(QPixmap("Locked.svg"))
        elif q.scheme() == "http":
            self.ssl_icon.setPixmap(QPixmap("UnLocked.svg"))
        else:
            q.setScheme("https")

        self.tabs.currentWidget().setUrl(q)
    
    #Check SSL in the url bar.
    def ssl_check(self):
        q = QUrl(self.urlbar.text())

        if q.scheme() == "https":
            self.ssl_icon.setPixmap(QPixmap("Locked.svg"))
        elif q.scheme() == "http":
            self.ssl_icon.setPixmap(QPixmap("UnLocked.svg"))
        else:
            q.setScheme("https")
        
    #Method to update the url.
    def update_urlbar(self, q, browser = None):
 
        #If this signal is not from the current tab then ignore it.
        if browser != self.tabs.currentWidget():
            return
 
        #Set text to the url bar.
        self.urlbar.setText(q.toString())
 
        #Set cursor position.
        self.urlbar.setCursorPosition(0)
    
    #Method for opening local files that are on your computer.
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                "Hypertext Markup Language (*.htm *.html);;"
                "All files (*.*)")
        
        self.view = QtWebEngineWidgets.QWebEngineView()

        if filename:
            with open(filename, "r") as f:
                html = f.read()

            self.tabs.currentWidget().setUrl(QtCore.QUrl().fromLocalFile(filename))

            #Update the url bar.
            self.urlbar.setText(filename)

            #Update that title.
            self.update_title(self.tabs.currentWidget())
    
    def screenshot_page(self):
        w = QtWidgets.QTabWidget()
        #current_date_time = datetime.datetime.now()
        #screenshot_name = f"Screenshot {current_date_time}.png"
        screenshot_name = f"Screenshot.png"
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save(screenshot_name, "png")
        message = QMessageBox.about(self, "Screenshot Taken", "A Screenshot Of This Page Has Been Taken.")

    #Settings window being shown.
    def settings_window(self):
        #self.settings_win = SettingsWindow()
        #self.settings_win.show()
        self.widget = QWidget()
        self.widget.setWindowTitle("Settings Menu")
        self.widget.setWindowIcon(QtGui.QIcon("Logo.png"))
        self.widget.setGeometry(400, 400, 370, 400)

        #Settings file.
        self.configuration = ConfigParser()
        self.configuration.read("Settings.ini")
        if self.configuration.has_section("Settings"):
            pass
        else:
            self.configuration.add_section("Settings")
        if self.configuration.has_option("Settings", "js_setting"):
            pass
        else:
            self.configuration.set("Settings", "js_setting", "True")
        if self.configuration.has_option("Settings", "autoplay_setting"):
            pass
        else:
            self.configuration.set("Settings", "autoplay_setting", "False")
        if self.configuration.has_option("Settings", "animated_setting"):
            pass
        else:
            self.configuration.set("Settings", "animated_setting", "False")
        if self.configuration.has_option("Settings", "proxy_setting"):
            pass
        else:
            self.configuration.set("Settings", "proxy_setting", "True")
        if self.configuration.has_option("Settings", "search_setting"):
            pass
        else:
            self.configuration.set("Settings", "search_setting", SEARCH)
        if self.configuration.has_option("Settings", "theme_setting"):
            pass
        else:
            self.configuration.set("Settings", "theme_setting", THEME)

        with open("Settings.ini", "w") as f:
            self.configuration.write(f)

        #Settings label.
        label = QLabel("Settings Menu", self.widget)
        label.move(10, 2)
        label.show()

        #Java script setting.
        js_on = QCheckBox("Java Script", self.widget)
        js_on.move(20, 20)
        js_on.resize(320, 40)
        js_on.stateChanged.connect(self.js_on_changed)

        if self.configuration.get("Settings", "js_setting") == "True":
            js_on.setChecked(True)
        else:
            js_on.setChecked(False)

        #Auto play setting.
        auto_play_on = QCheckBox("Auto Play", self.widget)
        auto_play_on.move(20, 50)
        auto_play_on.resize(320, 40)
        auto_play_on.stateChanged.connect(self.auto_play_on_changed)

        if self.configuration.get("Settings", "autoplay_setting") == "True":
            auto_play_on.setChecked(True)
        else:
            auto_play_on.setChecked(False)

        #Animated scroll bars setting.
        animated_scroll_bars_on = QCheckBox("Animated Scroll Bars", self.widget)
        animated_scroll_bars_on.move(20, 80)
        animated_scroll_bars_on.resize(320, 40)
        animated_scroll_bars_on.stateChanged.connect(self.animated_scroll_bars_on_changed)

        if self.configuration.get("Settings", "animated_setting") == "True":
            animated_scroll_bars_on.setChecked(True)
        else:
            animated_scroll_bars_on.setChecked(False)

        #Proxy setting
        proxy_on = QCheckBox("Proxy Service", self.widget)
        proxy_on.move(20, 110)
        proxy_on.resize(320, 40)
        proxy_on.stateChanged.connect(self.proxy_on_changed)

        if self.configuration.get("Settings", "proxy_setting") == "True":
            proxy_on.setChecked(True)
        else:
            proxy_on.setChecked(False)

        #Search engine choice label.
        search_engine_label = QLabel("Search Engine Choice", self.widget)
        search_engine_label.move(10, 170)
        search_engine_label.show()

        #Search engine choice setting.
        self.search_engine = QComboBox(self.widget)
        self.search_engine.addItem("Search Engine Choice")
        self.search_engine.addItem("Brave Search")
        self.search_engine.addItem("SearX")
        self.search_engine.addItem("Swisscows")
        self.search_engine.addItem("Startpage")
        self.search_engine.addItem("Duck Duck Go")
        self.search_engine.addItem("MetaGer")
        self.search_engine.addItem("Presearch")
        self.search_engine.addItem("Shodan")
        self.search_engine.addItem("Ecosia")
        self.search_engine.addItem("Mojeek")
        self.search_engine.move(20, 200)
        self.search_engine.resize(320, 40)
        self.search_engine.currentIndexChanged.connect(self.search_engine_changed)

        if self.configuration.get("Settings", "search_setting") == "https://search.brave.com/search?q=":
            self.search_engine.setCurrentIndex(1)
        elif self.configuration.get("Settings", "search_setting") == "https://searx.xyz/search?q=":
            self.search_engine.setCurrentIndex(2)
        elif self.configuration.get("Settings", "search_setting") == "https://swisscows.com/web?culture=en&query=":
            self.search_engine.setCurrentIndex(3)
        elif self.configuration.get("Settings", "search_setting") == "https://www.startpage.com/search?query=":
            self.search_engine.setCurrentIndex(4)
        elif self.configuration.get("Settings", "search_setting") == "https://duckduckgo.com/?q=":
            self.search_engine.setCurrentIndex(5)
        elif self.configuration.get("Settings", "search_setting") == "https://metager.org/meta/meta.ger3?eingabe=":
            self.search_engine.setCurrentIndex(6)
        elif self.configuration.get("Settings", "search_setting") == "https://presearch.com/search?q=":
            self.search_engine.setCurrentIndex(7)
        elif self.configuration.get("Settings", "search_setting") == "https://www.shodan.io/search?query=":
            self.search_engine.setCurrentIndex(8)
        elif self.configuration.get("Settings", "search_setting") == "https://www.ecosia.org/search?q=":
            self.search_engine.setCurrentIndex(9)
        elif self.configuration.get("Settings", "search_setting") == "https://www.mojeek.com/search?q=":
            self.search_engine.setCurrentIndex(10)
        else:
            self.search_engine.setCurrentIndex(0)

        #Theme choice label.
        theme_label = QLabel("Theme Choice", self.widget)
        theme_label.move(10, 260)
        theme_label.show()

        #Theme choice setting.
        self.theme = QComboBox(self.widget)
        self.theme.addItem("Theme Choice")
        self.theme.addItem("Light")
        self.theme.addItem("Dark")
        self.theme.addItem("Neon")
        self.theme.addItem("Fresh")
        self.theme.addItem("Cherry")
        self.theme.addItem("Forest")
        self.theme.addItem("Majestic")
        self.theme.move(20, 290)
        self.theme.resize(320, 40)
        self.theme.currentIndexChanged.connect(self.theme_changed)

        if self.configuration.get("Settings", "theme_setting") == "Light":
            self.theme.setCurrentIndex(1)
        elif self.configuration.get("Settings", "theme_setting") == "Dark":
            self.theme.setCurrentIndex(2)
        elif self.configuration.get("Settings", "theme_setting") == "Neon":
            self.theme.setCurrentIndex(3)
        elif self.configuration.get("Settings", "theme_setting") == "Fresh":
            self.theme.setCurrentIndex(4)
        elif self.configuration.get("Settings", "theme_setting") == "Cherry":
            self.theme.setCurrentIndex(5)
        elif self.configuration.get("Settings", "theme_setting") == "Forest":
            self.theme.setCurrentIndex(6)
        elif self.configuration.get("Settings", "theme_setting") == "Majestic":
            self.theme.setCurrentIndex(7)
        else:
            self.theme.setCurrentIndex(0)

        #Creating the save settings button.
        self.save_button = QPushButton(self.widget)
        self.save_button.setText("Save")
        self.save_button.move(10, 360)
        self.save_button.clicked.connect(self.save_settings)
        self.save_button.setShortcut("Ctrl+S")

        #Making the cancel settings button.
        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setText("Cancel")
        self.cancel_button.move(100, 360)
        self.cancel_button.clicked.connect(self.cancel_settings)
        self.cancel_button.setShortcut("Ctrl+J")

        #Show the settings window.
        self.widget.show()

    #The settings can be changed with it.
    def js_on_changed(self, state):
        if (QtCore.Qt.Checked == state):
            print("\nJava Script On.")
            self.websettings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
            self.configuration.set("Settings", "js_setting", "True")
        else:
            print("\nJava Script Off.")
            self.websettings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)
            self.configuration.set("Settings", "js_setting", "False")
        
        with open("Settings.ini", "w") as f:
            self.configuration.write(f)
    
    def auto_play_on_changed(self, state):
        if (QtCore.Qt.Checked == state):
            print("\nAuto Play On.")
            self.websettings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, True)
            self.configuration.set("Settings", "autoplay_setting", "True")
        else:
            print("\nAuto Play Off.")
            self.websettings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
            self.configuration.set("Settings", "autoplay_setting", "False")
        
        with open("Settings.ini", "w") as f:
            self.configuration.write(f)

    def animated_scroll_bars_on_changed(self, state):
        if (QtCore.Qt.Checked == state):
            print("\nAnimated Scroll Bars On.")
            self.websettings.setAttribute(QWebEngineSettings.ScrollAnimatorEnabled, True)
            self.configuration.set("Settings", "animated_setting", "True")
        else:
            print("\nAnimated Scroll Bars Off.")
            self.websettings.setAttribute(QWebEngineSettings.ScrollAnimatorEnabled, False)
            self.configuration.set("Settings", "animated_setting", "False")
        
        with open("Settings.ini", "w") as f:
            self.configuration.write(f)
    
    def proxy_on_changed(self, state):
        self.proxy = QtNetwork.QNetworkProxy()
        if (QtCore.Qt.Checked == state):
            print("\nProxy Service On.")
            self.proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
            self.proxy.setHostName(PROXY_IP)
            self.proxy.setPort(int(PROXY_PORT))
            QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
            self.configuration.set("Settings", "proxy_setting", "True")
        else:
            print("\nProxy Service Off.")
            self.proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
            self.proxy = QtNetwork.QNetworkProxy()
            QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
            self.configuration.set("Settings", "proxy_setting", "False")
        
        with open("Settings.ini", "w") as f:
            self.configuration.write(f)
    
    def search_engine_changed(self):
        item = self.search_engine.currentText()
        if item == "Search Engine Choice":
            self.homepage = "https://search.brave.com/"
            self.search_engine_choice = "https://search.brave.com/search?q="
            print("\nSearch Engine Changed To Brave Search.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Brave Search":
            self.homepage = "https://search.brave.com/"
            self.search_engine_choice = "https://search.brave.com/search?q="
            print("\nSearch Engine Changed To Brave Search.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "SearX":
            self.homepage = "https://searx.xyz/"
            self.search_engine_choice = "https://searx.xyz/search?q="
            print("\nSearch Engine Changed To SearX.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Swisscows":
            self.homepage = "https://swisscows.com/"
            self.search_engine_choice = "https://swisscows.com/web?culture=en&query="
            print("\nSearch Engine Changed To Swisscows.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Startpage":
            self.homepage = "https://www.startpage.com/"
            self.search_engine_choice = "https://www.startpage.com/search?query="
            print("\nSearch Engine Changed To Startpage.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Duck Duck Go":
            self.homepage = "https://duckduckgo.com/"
            self.search_engine_choice = "https://duckduckgo.com/?q="
            print("\nSearch Engine Changed To Duck Duck Go.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "MetaGer":
            self.homepage = "https://metager.org/"
            self.search_engine_choice = "https://metager.org/meta/meta.ger3?eingabe="
            print("\nSearch Engine Changed To MetaGer.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Presearch":
            self.homepage = "https://presearch.com/"
            self.search_engine_choice = "https://presearch.com/search?q="
            print("\nSearch Engine Changed To Presearch.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Shodan":
            self.homepage = "https://www.shodan.io/"
            self.search_engine_choice = "https://www.shodan.io/search?query="
            print("\nSearch Engine Changed To Shodan.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Ecosia":
            self.homepage = "https://www.ecosia.org/"
            self.search_engine_choice = "https://www.ecosia.org/search?q="
            print("\nSearch Engine Changed To Ecosia.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        elif item == "Mojeek":
            self.homepage = "https://www.mojeek.com/"
            self.search_engine_choice = "https://www.mojeek.com/search?q="
            print("\nSearch Engine Changed To Mojeek.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        else:
            self.homepage = "https://search.brave.com/"
            self.search_engine_choice = "https://search.brave.com/search?q="
            print("\nSearch Engine Changed To Brave Search.")
            self.configuration.set("Settings", "search_setting", self.search_engine_choice)
        
        with open("Settings.ini", "w") as f:
            self.configuration.write(f)

    def theme_changed(self):
        item = self.theme.currentText()
        if item == "Theme Choice":
            self.theme_choice = "Light"
            print("\nTheme Changed To Light.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Light":
            self.theme_choice = "Light"
            print("\nTheme Changed To Light.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Dark":
            self.theme_choice = "Dark"
            print("\nTheme Changed To Dark.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Neon":
            self.theme_choice = "Neon"
            print("\nTheme Changed To Neon.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Fresh":
            self.theme_choice = "Fresh"
            print("\nTheme Changed To Fresh.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Cherry":
            self.theme_choice = "Cherry"
            print("\nTheme Changed To Cherry.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Forest":
            self.theme_choice = "Forest"
            print("\nTheme Changed To Forest.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        elif item == "Majestic":
            self.theme_choice = "Majestic"
            print("\nTheme Changed To Majestic.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        else:
            self.theme_choice = "Light"
            print("\nTheme Changed To Light.")
            self.configuration.set("Settings", "theme_setting", self.theme_choice)
        
        with open("Settings.ini", "w") as f:
            self.configuration.write(f)
    
    #Settings actions with it.
    def save_settings(self, state):
        #self.js_on_changed(state)
        #self.auto_play_on_changed(state)
        #self.animated_scroll_bars_on_changed(state)
        #self.ad_blocker_on_changed(state)
        #self.search_engine_changed()
        #self.theme_changed()

        self.widget.close()
        
        message = QMessageBox.about(self, "Settings Saved", "Your Settings Have Been Saved.")
    
    def cancel_settings(self):
        self.widget.close()

#Creating a PyQt5 application.
app = QApplication(sys.argv)

#Theme chooser.
configuration = ConfigParser()
configuration.read("Settings.ini")
theme = configuration.get("Settings", "theme_setting")

if theme == "Light":
    app.setStyle("Fusion")
elif theme == "Dark":
    app.setStyleSheet(open("night_theme.qss", "r").read())
elif theme == "Neon":
    app.setStyleSheet(open("neon_theme.qss", "r").read())
elif theme == "Fresh":
    app.setStyleSheet(open("fresh_theme.qss", "r").read())
elif theme == "Cherry":
    app.setStyleSheet(open("cherry_theme.qss", "r").read())
elif theme == "Forest":
    app.setStyleSheet(open("forest_theme.qss", "r").read())
elif theme == "Majestic":
    app.setStyleSheet(open("classy_theme.qss", "r").read())
else:
    app.setStyle("Fusion")
 
#Setting name to the application.
app.setApplicationName("Viridium |  By:  ViridianTelamon")
 
#Creating MainWindow object.
window = MainWindow()

#The Application.
app.exec_()
