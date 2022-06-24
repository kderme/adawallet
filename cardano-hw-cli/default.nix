{ stdenv, lib, fetchurl, patchelf, libusb, udev }:

let
  version = "1.10.0-rc1";
in stdenv.mkDerivation {
  pname = "cardano-hw-cli";
  version = "v${version}";
  src = fetchurl {
    url = "https://github.com/vacuumlabs/cardano-hw-cli/releases/download/v${version}/cardano-hw-cli-${version}_linux-x64.tar.gz";

    sha256 = "sha256-ZtQenffIjZIdZnBL+ykavfXR3uMd8VjFU5Ccnj8bqk4=";
  };
  phases = [ "unpackPhase" "installPhase" ];
  #sourceRoot = ".";
  installPhase = ''
    BASH_COMPLETIONS=$out/share/bash-completion/completions
    mkdir -p $out/bin
    mkdir -p "$BASH_COMPLETIONS"
    patchelf --set-interpreter ${stdenv.cc.libc}/lib/ld-linux-x86-64.so.2 cardano-hw-cli
    patchelf --set-rpath ${lib.makeLibraryPath [ stdenv.cc.cc libusb udev ]} cardano-hw-cli
    patchelf --set-rpath ${lib.makeLibraryPath [ stdenv.cc.cc libusb udev ]} Release/HID.node
    patchelf --set-rpath ${lib.makeLibraryPath [ stdenv.cc.cc libusb udev ]} Release/HID_hidraw.node
    cp cardano-hw-cli $out/bin/cardano-hw-cli
    cp -a Release $out/bin/
    cp package.json $out/bin//package.json
    cp ${./autocomplete.sh} $BASH_COMPLETIONS/cardano-hw-cli


  '';
}
