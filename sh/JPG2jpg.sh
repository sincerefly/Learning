#! /bin/sh 
# Usage: ./low.sh <-l | -u> <target_directory> 
#./low.sh -l directory 为全部转化为小写 
#./low.sh -u directory 为全部转化为大写 
# 
# 第二形参必须是目录，第一形参指定-l或-u 
# 
if [ $# -ne 2 ] ; then 
  echo "Usage: ${0} <-l | -u> <target_directory>" 
  exit 1 
fi 
if [ ! -d ${2} -o "${1}" != "-l" -a "${1}" != "-u" ] ; then 
  echo "Usage: ${0} <-l | -u> <target_directory>" 
  exit 1 
fi 
dir=`dirname "${2}"` 
cd ${dir} > /dev/null 2>&1 
if [ $? -ne 0 ] ; then 
  echo "Error: checking your ${dir}" 
  exit 1 
fi 
exec 1>/dev/null 2>&1 
if [ "${1}" = "-l" ] ; then 
  base=`basename "${2}" | tr "[A-Z]" "[a-z]"` 
else 
  base=`basename "${2}" | tr "[a-z]" "[A-Z]"` 
fi 
mv -f "`basename ${2}`" "${base}" > /dev/null 2>&1 
for entry in `find ${base}` 
do 
  before="." 
  for after in `echo "${entry}" | sed -e 's,/, ,g'` 
  do 
    tmp_entry="${before}/${after}" 
    if [ "${1}" = "-l" ] ; then 
      before=`echo "${tmp_entry}" | tr "[A-Z]" "[a-z]"` 
    else 
      before=`echo "${tmp_entry}" | tr "[a-z]" "[A-Z]"` 
    fi 
    mv -f "${tmp_entry}" "${before}" 
  done 
done
    fi
  done
done
fi
