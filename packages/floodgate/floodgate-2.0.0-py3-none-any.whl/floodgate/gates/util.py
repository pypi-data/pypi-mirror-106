def raise_package_error(name):
    raise ImportError(
        f"Cannot find {name}\n\neither install floodgate via \npip install floodgate[{name}] or install {name} directly via \npip install {name}"
    )
