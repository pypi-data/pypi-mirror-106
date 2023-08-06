# -*- coding: utf-8 -*-

# 
#  
# Do your import here
#
#

def parse_data_ref(data_ref):
  """
    :param data_ref: output reference as string
    :return:
  """

  #
  #
  # Parse your data reference
  #
  #

def run(data_path, data_ref, argument_1, argument_2, argument_3, test=False):
    """
      :param data_path: path to data directory (string)
      :param data_ref: output reference (string)
      :param argmuent1:
      :param argument2:
      :param argument3:
      :test: Activate service test mode
      :return:
    """

    info = parse_data_ref(data_ref)

    if test :
      #
      # Run your service in test mode
      #

      return 
   
    #
    #
    # Python code for the service in normal mode goes here !
    #
    #

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])

__all__ = ["run"]