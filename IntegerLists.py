class IntegerLists:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        occurrences = dict()
        occurrences["most_common"] = []
        for num in nums:
            # print(str(num) + " " + str(occurrences["most_common"]))
            occurrences[num] = occurrences[num] + 1 if num in occurrences.keys() else 1
            if len(occurrences["most_common"]) < k:
                if num not in occurrences["most_common"]:
                    occurrences["most_common"].append(num)
            else:
                if num not in occurrences["most_common"]:
                    occurrences["most_common"].append(num)
                    minim_count = occurrences[num]
                    minim_index = num

                    for n in occurrences["most_common"]:
                        if occurrences[n] < minim_count:
                            minim_count = occurrences[n]
                            minim_index = n

                    occurrences["most_common"].remove(minim_index)
                
                    
        return occurrences["most_common"]
                