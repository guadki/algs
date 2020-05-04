package algs.mat

import org.scalatest.funsuite.AnyFunSuite

class MultiplyTest extends AnyFunSuite with Multiply {

  test("Multiplying empty vectors returns empty vector") {
    assert(multiply(Vector.empty, Vector.empty) == Vector.empty)
  }

  test("Multiplying by empty vectors returns empty vector") {
    assert(multiply(Vector(Vector(1, 2)), Vector.empty) == Vector.empty)
  }

  test("Multiplying empty vector returns empty vector") {
    assert(multiply(Vector.empty, Vector(Vector(1, 2))) == Vector.empty)
  }

  test("Multiplying square mats should work") {
    assert(
      multiply(
        Vector(
          Vector(1, 2, 3),
          Vector(4, 5, 6),
          Vector(7, 8, 9)
        ),
        Vector(
          Vector(2, 4, 6),
          Vector(1, 3, 5),
          Vector(7, 4, 3))) ==
        Vector(
          Vector(25, 22, 25),
          Vector(55, 55, 67),
          Vector(85, 88, 109))
    )
  }

  test("Multiplying non-square mats should work") {
    assert(
      multiply(
        Vector(
          Vector(1, 2, 3),
          Vector(4, 5, 6)
        ),
        Vector(
          Vector(2, 4),
          Vector(6, 8),
          Vector(3, 5))) ==
        Vector(
          Vector(23, 35),
          Vector(56, 86))
    )
  }

  test("Wrong sized mats should throw an exception") {
    assertThrows[IllegalArgumentException](
      multiply(
        Vector(
          Vector(1, 2, 3),
          Vector(4, 5, 6)
        ),
        Vector(
          Vector(2, 4),
          Vector(6, 8)))
    )
  }


}
