{ pkgs }: {
  deps = [
    pkgs.python311Full
    pkgs.python311Packages.fastapi
    pkgs.python311Packages.uvicorn
    pkgs.python311Packages.pip
  ];
}
