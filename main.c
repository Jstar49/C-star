#include <stdio.h>
long long result = 7249970239362560142;
int main() {
  /* ===== Block 1 ===== */
  short var_1_0 = 31321;
  int var_1_1 = -1189752394;
  unsigned char var_1_2 = 49;
  unsigned int var_1_3 = 3814136147;
  var_1_3 &= ((var_1_3&var_1_2)<<(var_1_3^var_1_1));
  
  /* ===== Block 2 ===== */
  unsigned int var_2_0 = 2017366661;
  int var_2_1 = -1981032977;
  var_1_0 |= (var_1_2<<var_1_0);
  var_1_3 |= (var_2_1>>var_1_2);
  var_2_0 ^= (var_2_1*var_2_0);
  
  /* ===== Block 3 ===== */
  long var_3_0 = -1102872405;
  int var_3_1 = -1970469698;
  var_1_0 &= (((var_3_1/var_1_3)+(((var_1_3>>var_1_2)^((var_1_1/var_1_0)/(var_3_0%var_2_0)))%(((var_1_3|var_2_1)-(var_1_1|var_1_2))*((var_2_1<<var_1_1)-(var_1_0*var_2_1)))))<<(var_1_2<<var_3_1));
  
  result /= (var_2_1%var_3_0);
  printf("RESULT : %4X\n", result);
}
