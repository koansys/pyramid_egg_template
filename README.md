# atemplate README


## Downloaded
grab a tarball from [https://github.com/koansys/pyramid__egg_template/tarball/x.x.x] (https://github.com/koansys/pyramid__egg_template/tarball/x.x.x)
replacing x.x.x whatever the current version is


## Cloned
or if you have atemplate cloned run::

  - $ git checkout-index -a -f --prefix=/path/to/mypackage_name/
  
## Then set it up

  - $ cd /path/to/mypackage_name
  - $ mv atemplate mypackage_name
  - $ perl -p -i -e "s/atemplate/mypackage_name/g" `grep -ril atemplate *`