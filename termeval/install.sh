cargo build --release
echo "copying to /usr/bin"
doas cp target/release/termeval /usr/bin
echo "creating symlink to '='"
doas ln -s /usr/bin/termeval /usr/bin/=
