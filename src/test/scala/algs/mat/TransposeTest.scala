package algs.mat

import org.scalatest.funsuite.AnyFunSuite

class TransposeTest extends AnyFunSuite with Transpose {

  test("Transposing empty vector returns empty vector") {
    assert(transpose(Vector.empty) == Vector.empty)
  }

  test("Transposing vector should work") {
    assert(transpose(Vector(Vector(1, 2, 3))) == Vector(Vector(1), Vector(2), Vector(3)))
  }

  test("Transposing square matrix should work") {
    assert(
      transpose(
        Vector(
          Vector(1, 2, 3),
          Vector(4, 5, 6),
          Vector(7, 8, 9))) ==
        Vector(
          Vector(1, 4, 7),
          Vector(2, 5, 8),
          Vector(3, 6, 9)))
  }

  test("Non-matrix input should throw an exception") {
    assertThrows[IllegalArgumentException](
      transpose(
        Vector(
          Vector(1, 2, 3),
          Vector(4, 5),
          Vector(7, 8, 9)))
    )
  }

  test("Transpose should work for big inputs") {
    val mat = Vector(
      Vector.from(0 to 1000000),
      Vector.from(0 to 1000000),
      Vector.from(0 to 1000000))
    assert(transpose(mat) == mat.transpose)
  }

}
