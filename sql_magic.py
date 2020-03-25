from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

# More docs in https://ipython.org/ipython-doc/3/config/custommagics.html
@magics_class
class SqlMagic(Magics):

  def __init__(self, shell, spark):
    super(SqlMagic, self).__init__(shell)
    self.spark = spark

  @line_cell_magic
  def sql(self, line, cell=None):
    if cell is None:
      sqlText = line
    else:
      sqlText = cell.replace("\n", " ")
    self.spark.sql(sqlText).show()

def register(spark):
  ip = get_ipython()
  magics = SqlMagic(ip, spark)
  ip.register_magics(magics)
