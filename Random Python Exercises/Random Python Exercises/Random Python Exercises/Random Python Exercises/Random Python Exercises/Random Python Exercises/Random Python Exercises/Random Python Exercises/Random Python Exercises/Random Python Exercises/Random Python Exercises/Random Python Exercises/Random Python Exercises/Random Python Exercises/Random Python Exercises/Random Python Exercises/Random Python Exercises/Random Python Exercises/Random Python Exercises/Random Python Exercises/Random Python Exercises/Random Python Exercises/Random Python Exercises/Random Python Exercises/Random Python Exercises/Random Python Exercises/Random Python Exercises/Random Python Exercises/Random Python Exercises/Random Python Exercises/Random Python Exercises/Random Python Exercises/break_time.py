def main():
    import time
    import webbrowser

    break_count = 0
    total_breaks = 3
    print "This program started on "+ time.ctime()
    while (break_count < total_breaks):
        time.sleep(5)
        webbrowser.close("https://www.youtube.com/watch?v=t03wigE8GK0")
        break_count += 1

main()
