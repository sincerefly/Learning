#include <stdio.h>
#include <locale.h>
#include <libintl.h>

/*使用gettext通常使用类似下面的一个带函数的宏定义
  *你完全可以不用，直接使用 gettext(字符串)
*/
#define _(S) gettext(S)

/*PACKAGE是本程序最终的名字（运行时输入的命令）*/
#define PACKAGE "jian_gettext"

int main(int argc, char **argv)
{
  /* 下面三个参数都是使用gettext时候需要使用的
    * setlocale
    * bindtextdomain
    * textdomain
  */
  setlocale(LC_ALL,"");
  bindtextdomain(PACKAGE, "locale");
  textdomain(PACKAGE);

  printf(_("Hello,GetText!\n"));
  return 0;
}
