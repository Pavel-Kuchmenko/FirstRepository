def connection(ip, port):
    def printer(func):
        def inner(doc):
            print(f"Connected to IP: {ip}:{port}")
            print(f"I am {func.__name__}")
            func(doc)
            print(f"Close connection...")
        return inner
    return printer

@connection(ip="192.168.0.2", port="8888")
def hp(document):
    print(f"Printing: {document}")

@connection(ip="192.168.0.3", port="8008")
def canon(document):
    print(f"Printing: {document}")


hp("text.doc")
canon("document.txt")