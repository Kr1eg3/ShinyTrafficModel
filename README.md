# ShinyTrafficModel
Реализация модели трафика  S-NFS 




```
                  __..-======-------..__
              . '    ______    ___________`.
            .' .--. '.-----.`. `.-----.-----`.
           / .'   | ||      `.` \\     \     \\            _
         .' /     | ||        \\ \\_____\_____\\__________[_]
        /   `-----' |'---------`\  .'                       \
       /============|============\'-------------------.._____|
    .-`---.         |-==.        |'.__________________  =====|-._
  .'        `.      |            |      .--------.    _` ====|  _ .
 /     __     \     |            |   .'           `. [_] `.==| [_] \
[   .`    `.  |     |            | .'     .---.     \      \=|     |
|  | / .-. '  |_____\___________/_/     .'---. `.    |     | |     |
 `-'| | O |'..`------------------'.....'/ .-. \ |    |       ___.--'
     \ `-' / /   `._.'                 | | O | |'___...----''___.--'
      `._.'.'                           \ `-' / [___...----''_.'
```




### Linux 64-bit


#### Quick start, installing all completers

- Install YCM plugin via [Vundle][]
- Install cmake, vim and python

```
apt install build-essential cmake vim-nox python3-dev
```

- Install mono-complete, go, node, java and npm

```
apt install mono-complete golang nodejs default-jdk npm
```

- Compile YCM

```
cd ~/.vim/bundle/YouCompleteMe
python3 install.py --all
```

- For plugging an arbitrary LSP server, check [the relevant section](#plugging-an-arbitrary-lsp-server)
