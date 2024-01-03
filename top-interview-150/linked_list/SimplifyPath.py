class SimplifyPath:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == ".." and stack:
                stack.pop()
            elif p not in ["", ".", ".."]:
                stack.append(p)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    init = SimplifyPath()
    print(init.simplifyPath("/home/"))  # /home
    print(init.simplifyPath("/../"))  # /
    print(init.simplifyPath("/home//foo/"))  # /home/foo
