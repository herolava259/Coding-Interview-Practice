
namespace CSharpWithAlgorithm.Arrays;

public static class SearchInRotatedArrayIIProblem
{
    private static int Clip(this int val, int low = int.MinValue, int high = int.MaxValue)
        => val switch
        {
            var v when v < low => low,
            var v when v > high => high,
            _ => val
        };
    public static int FragmentSearch<TElement>(this IList<TElement> elements,
                                             Func<int, int, int> middleIndexSelector,
                                             Func<TElement, TElement, TElement, int> exclusiveCondition,
                                             Func<TElement, TElement, int> cornerCondition,
                                             bool includeMiddle = false,
                                             int initialLowIdx = 0,
                                             int initialHighIdx = -1)
    {
        var low = initialLowIdx;
        var high = initialHighIdx == -1 ? elements.Count - 1 : initialHighIdx;

        while (low < high - 1)
        {
            var mid = middleIndexSelector(low, high);

            switch (exclusiveCondition(elements[low], elements[high], elements[mid]))
            {
                case 0:
                    return mid;
                case 1:
                    high = (mid - (includeMiddle ? 0 : 1)).Clip(low, high);
                    break;
                case -1:
                    low = (mid + (includeMiddle ? 0 : 1)).Clip(low, high);
                    break;
                default:
                    throw new ArgumentException("exclusiveCondition is invalid");
            }
        }

        return cornerCondition(elements[low], elements[high]) switch
        {
            0 => low,
            1 => high,
            _ => -1
        };
    }


    public static int FragmentSearch<TElement>(this IList<TElement> source,
                                                   Func<int, int, int> pivotIndexSelector,
                                                   Func<(int, TElement), (int, TElement), (int, TElement), (int, int)> rangeSelector,
                                                   Func<TElement, bool>? elementCondition = null,
                                                   Func<TElement, TElement, bool>? cornerCondition = null,
                                                   int initialLowIdx = 0,
                                                   int initialHighIdx = -1)
    {
        var low = initialLowIdx;
        var high = initialHighIdx != -1 ? initialHighIdx : source.Count - 1;

        if (elementCondition == null)
            elementCondition = (_) => false;

        if (cornerCondition == null)
            cornerCondition = (_, _) => true;

        while (low < high - 1)
        {
            var pivot = pivotIndexSelector(low, high);

            if (elementCondition(source[pivot]))
                return pivot;

            (low, high) = rangeSelector((low, source[low]), (high, source[high]), (pivot, source[pivot]));
        }

        return cornerCondition(source[low], source[high]) ? low : high;
    }
    public static bool Search(int[] nums, int target)
    {
        // find arg(position) of min element in nums arr
        var argMin = nums.FragmentSearch((begIdx, endIdx) => (begIdx + endIdx) >> 1,
                                                  (low, high, mid) =>
                                                  {
                                                      var (lowIdx, lowVal) = low;
                                                      var (highIdx, highVal) = high;
                                                      var (midIdx, midVal) = mid;

                                                      // corner case: need to linear search 
                                                      // ie: nums = [1,0,1,1] and target = 0
                                                      // rule below not corrected in the case
                                                      if (lowVal == highVal && midVal == lowVal)
                                                          return (lowIdx + 1, highIdx);

                                                      return (lowVal >= highVal, midVal >= lowVal) switch
                                                      {
                                                          (true, true) => (midIdx + 1, highIdx),
                                                          (true, false) => (lowIdx + 1, midIdx),
                                                          _ => (lowIdx, (midIdx - 1).Clip(low: lowIdx))
                                                      };

                                                  },
                                                  elementCondition: midVal => midVal == target,
                                                  cornerCondition: (lowVal, highVal) => lowVal < highVal);


        if (nums[argMin] == target)
            return true;
        else if (nums[argMin] > target)
            return false;

        while (argMin > 0 && nums[argMin] == nums[argMin - 1])
            argMin--;
        var (lowIdx, highIdx) = (0, nums.Length - 1);

        // case: if there are two distinct non-decrease fragment arrays
        if (argMin > 0)
        {
            (lowIdx, highIdx) = nums[0] > target ? (argMin, nums.Length - 1)
                                                 : (0, argMin - 1);
        }

        return nums.FragmentSearch((l, h) => (l + h) >> 1,
                                        (_, _, midVal) => midVal switch
                                        {
                                            var v when v == target => 0,
                                            var v when v < target => -1,
                                            _ => 1
                                        }
                                        ,
                                        (l, h) => (l == target, h == target) switch
                                        {
                                            (true, _) => 0,
                                            (_, true) => 1,
                                            _ => -1
                                        },
                                        initialLowIdx: lowIdx,
                                        initialHighIdx: highIdx) != -1;
    }
}
