import re
import configparser

if __name__ == "__main__":

    settings = "settings.ini"
    config = configparser.ConfigParser()
    config.read(settings)
    # # Writing Data
    # try:
    #     config.add_section("SETTINGS")
    # except configparser.DuplicateSectionError:
    #     pass
    #
    # config.set("SETTINGS", "file", r"C:\Users\24969\Desktop\shared_preferences.json")
    # config.set("SETTINGS", "pattern", r'https://flm88.site/(.*?)/(.*?)\\')
    # with open(settings, "w") as config_file:
    #     config.write(config_file)

    # Reading Data
    file = ""
    pattern = ""
    try:
        file = config.get("SETTINGS", "file")
        pattern = config.get("SETTINGS", "pattern")
        print(file, pattern)
    except configparser.NoOptionError:
        print(f"No option pattern in section 'SETTINGS'")

    data = open(file, 'r', encoding='utf8')
    line = data.read()
    results = re.finditer(pattern, line)
    print(results)
    for result in results:
        print(result.group())
    print("程序运行成功，按任意键退出。")
    input()
