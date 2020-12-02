if __name__ == "__main__":
    try:
        while True:
            src = input("> ") # use Ctrl_z (windows) or Ctrl_d (linux) to terminate the program.
            l = src.split(" ")
            l[0] = l[0][:-1] # 去掉数字后的实心点。
            s = "_".join(l)
            print(s)
            print("[{}](./src/{}.md)".format(src, s))
    except EOFError:
        pass # just avoid the error dump.