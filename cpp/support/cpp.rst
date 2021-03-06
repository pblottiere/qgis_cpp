Rappels de C++ (1)
==================

|

.. image:: imgs/bjarne.png
  :width: 140pt
  :align: center

- 1983 - Bjarne Stroustrup (Danois)
- Langage compilé orienté objet (et procédural)
- Typage statique
- Pas de garbage collector
- C++ 99 → C++ 11 → C++ 14 → C++ 17

Rappels de C++ (2)
==================

|

.. image:: imgs/cppenv.png
  :width: 1500pt
  :align: center

Rappels de C++ (3)
==================

|

**main**

.. code-block:: C++

  #include "hello.h"

  int main( int argc, char** argv)
  {
    const Hello h1( 1 );
    h1.print();

    const int n2 = 2;
    Hello *h2 = new Hello( n2 );
    h2->print();
    delete h2; // unique ptr?

    return 0;
  }

.. code-block:: bash

  $ ./main
  Hello 1
  Hello 2

Rappels de C++ (4)
==================

|

**Header** : déclaration

.. code-block:: C++

  #ifndef HELLO_H  // #pragma once
  #define HELLO_H

  class Hello
  {
    public:
      Hello( int number );
      ~Hello();

      void print() const;

    private:
      const int mNumber;
  };

  #endif

Rappels de C++ (5)
==================

|

**Source** : implémentation

.. code-block:: C++

  #include <iostream>
  #include "hello.h"

  Hello::Hello( const int number )
    : mNumber( number )
  {
  }

  Hello::~Hello()
  {
  }

  void Hello::print() const
  {
    std::cout << "Hello " <<  mNumber << std::endl;
  }

Rappels de C++ (6)
==================

|

**Méthode virtuelle pure ⟶ Classe abstraite**

.. code-block:: C++

  class HelloV2
  {
    public:
      HelloV2( const std::string &word );
      virtual ~HelloV2();

      virtual void print() const = 0;

    protected:
      void hello() const;

    private:
      const std::string mWord;
  }

Rappels de C++ (7)
==================

|

**Méthode virtuelle pure ⟶ Classe abstraite**

.. code-block:: C++

  HelloV2::HelloV2( const std::string &word )
    : mWord( word )
  {
  }

  HelloV2::~HelloV2()
  {
  }

  void HelloV2::hello() const
  {
    std::cout << "Hello " << mWord << "!" << std::endl;
  }

Rappels de C++ (8)
==================

|

**Héritage**

.. code-block:: C++

  class HelloWorldV2 : public HelloV2
  {
    public:
      HelloWorldV2();
      ~HelloWorldV2();

      void print() const override;
  };

Rappels de C++ (9)
==================

|

**Héritage**

.. code-block:: C++

  HelloWorldV2::HelloWorldV2()
    : HelloV2( "world!" )
  {
  }

  HelloWorldV2::~HelloWorldV2()
  {
  }

  void HelloWorldV2::print() const
  {
    std::cout << "HelloWorldV2 print: " << std::endl;
    HelloV2::hello();
  }

Rappels de C++ (10)
===================

|

**Surcharge / méthode statique**

.. code-block:: C++

  class Printer
  {
    static void hello( const HelloWorldV2 &h ) { h.print(); }
    static void hello( const Hello &h ) { h.print() ); }
  }

.. code-block:: C++

  int main( int argc, char** argv )
  {
    Hello h1( 10 );
    Printer::hello( h1 );

    HelloWorldV2 h2;
    Printer::hello( h2 );
  }

Rappels de C++ (11)
===================

|

**Sructures de contrôle : if**

.. code-block:: C++

  int a = ...;

  if ( a > 100 || a < 0 )
    a = 0;
  else if ( a == 42 )
    std::cout << "Awesome!" << std::endl;
  else
    std::cout << "Nothing todo" << std::endl;

Rappels de C++ (12)
===================

|

**Sructures de contrôle : switch/case**

.. code-block:: C++

  int a = ...;

  switch ( a )
  {
    case 1:
      std::cout << "a = 1" << std::endl;
      break;

    case 2:
      std::cout << "a = 2" << std::endl;
      break;

    default:
      std::cout << "Doesn't matter" << std::endl;
  }

Rappels de C++ (13)
===================

|

**Sructures de contrôle : for**

.. code-block:: C++

  # entier
  int a = 0;

  for ( int i = 0; i < 10; i++ )
    a += 1;

  # iterateur
  typedef std::list<int> Values;
  Values values;
  values.insert( values.begin(), 3 );
  values.insert( values.begin(), 30 );
  Values::iterator it;

  for( it = values.begin(); it != values.end(); it++ )
    a += *it;

  for( int value : values )
    a += value;

Rappels de C++ (14)
===================

|

**Sructures de contrôle : while**

.. code-block:: C++

  int i = 0;
  int a = 0;

  while ( i < 10 )
  {
    a += i;
    i++;
  }
