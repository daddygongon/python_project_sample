```{=org}
#+qiita_private: e47f263b43795cb7773a
```
```{=org}
#+STARTUP: indent nolineimagess overview num
```
```{=org}
#+TAG: Python, novice
```
```{=org}
#+TWITTER: off
```
```{=org}
#+SETUPFILE: https://fniessen.github.io/org-html-themes/org/theme-readtheorg.setup
```
# file open

-   path =\> \\ -\> /に変更必要
-   encoding = \'sjis\' ほんまかな，まぁ出力されているので．．．

# argv

``` python
import sys
sys.argv
```

なんですが，file pathを打ち間違うだろうから，そのままcodeを
変更させる方が間違いがなさそう．

自動で変換させましょうか．．． ARGVからとるので試しましょう．
Mikatypeはwindowsですので．

mikatype.logのパスですが， explorer.exeでPC-\> Local Diskを選んで，
そこで，mikatype.logを検索させるのが良さそう．

# scanf

parseライブラリ

``` example
pip install parse
```

が必要

# datetime

parse, strftimeとかね．

# final

```{=org}
#+name: ./python_codes/mikatype_log/mikatype_plot.py　
```
```{=org}
#+include: ./python_codes/mikatype_log/mikatype_plot.py src python :noweb yes
```
[![](./python_codes/mikatype_log/Figure_1.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/151211/63942db2-5c1c-8fdf-f77c-275096ab4cf4.png)
