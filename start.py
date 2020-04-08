import os, time

def start():
    print("   __                                _    _                            ")
    print("  / _|                              | |  | |                           ")
    print(" | |_  ___   _ __  _ __ ___    __ _ | |_ | |_  ___  _ __  _ __   _   _ ")
    print(" |  _|/ _ \ | '__|| '_ ` _ \  / _` || __|| __|/ _ \| '__|| '_ \ | | | |")
    print(" | | | (_) || |   | | | | | || (_| || |_ | |_|  __/| | _ | |_) || |_| |")
    print(" |_|  \___/ |_|   |_| |_| |_| \__,_| \__| \__|\___||_|(_)| .__/  \__, |")
    print("                                                         | |      __/ |")
    print("                                                         |_|     |___/ ")

def app():
    os.system("diskpart")
    time.sleep(5)
    os.system("disk list")
    

if __name__ == "__main__":
    start()
    app()