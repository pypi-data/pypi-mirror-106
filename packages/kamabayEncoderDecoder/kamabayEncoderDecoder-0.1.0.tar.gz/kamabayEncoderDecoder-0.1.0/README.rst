``KAMABAY`` ENCODE DECODE 
===========================


encode your data decode, KAMABAY ``encode decode based`` on ``dictionary``  you can change its output encode value by changing the value in its dictionary.


Encode
--------
.. code :: python
        
        from kamabay import KAMABAY_ENCODE_DECODE
        
        data = "hello world"# type data string
        save = True         # type boolean save file output data.kmy
        kamabay = KAMABAY_ENCODE_DECODE(
            data = data,
            save = save);
        print(kamabay.encode());

**output in file data.kmy and console** >  ``$dsew[KMY]fgdgf[KMY]me&yu[KMY]me&yu[KMY]p039=[KMY]4%32[KMY]^'-hd[KMY]p039=[KMY]3sdfh[KMY]me&yu[KMY]~gd!2[KMY]``

Decode
--------
.. code :: python
        
        from kamabay import KAMABAY_ENCODE_DECODE
        
        data = "data.kmy"
        save = False 
        kamabay = KAMABAY_ENCODE_DECODE(
            data = data,
            save = save);
        print(kamabay.decode());

**output** > ``hello world``

Show dictionary
----------------
.. code :: python
        
        from kamabay.KAMABAY_ENCODE_DECODE import showDict
        
        print(showDict(auth="KAMABAY"))

**output displays the json dictionary!**



``@copyright 21052021``

`repository github`_ | `licence`_ apache 2.0 | ``mail`` `lexyong66@gmail.com`_ 

.. _lexyong66@gmail.com : lexyong66@gmail.com
.. _repository github : https://github.com/ExsoKamabay/EncoderDecoder
.. _licence : https://www.apache.org/licenses/LICENSE-2.0