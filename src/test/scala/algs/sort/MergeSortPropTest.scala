package algs.sort

import algs.list.BasicListOps
import org.scalacheck.Prop.forAll
import org.scalacheck.Properties

object MergeSortPropTest extends Properties("BasicListOpsTest") with MergeSort with BasicListOps{

  property("MergeSort should sort elements in list") = forAll { input: List[Int] =>
    isSorted(sort(input))
  }

}
