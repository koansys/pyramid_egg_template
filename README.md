# atemplate README


## Downloaded
grab a tarball from [https://github.com/koansys/pyramid__egg_template/tarball/x.x.x] (https://github.com/koansys/pyramid__egg_template/tarball/x.x.x)
replacing x.x.x whatever the current version is and untar it

 - $ curl https://github.com/koansys/pyramid__egg_template/tarball/1.0 | tar zxf -


## Cloned

or if you have atemplate cloned *git clone git@github.com:koansys/pyramid_egg_template.git* run

  - $ git checkout-index -a -f --prefix=/path/to/mypackage_name/
  
## Then set it up

  - $ cd /path/to/mypackage_name
  - $ mv atemplate mypackage_name
  - $ perl -p -i -e "s/atemplate/mypackage_name/g" `grep -ril atemplate *`