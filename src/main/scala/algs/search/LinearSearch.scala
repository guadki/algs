package algs.search

trait LinearSearch {

  def search(array: Array[Int], v: Int): Option[Int] = {
    for {i <- array.indices} {
      if (array(i) == v) return Some(i)
    }

    None
  }

}
