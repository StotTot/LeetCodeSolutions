class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:

        ransomNoteFreq = {}
        magazineFreq = {}
        for i in ransomNote:
            ransomNoteFreq[i] = ransomNoteFreq.get(i, 0) + 1
        for j in magazine:
            magazineFreq[j] = magazineFreq.get(j, 0) + 1

        for i in ransomNoteFreq.keys():
            if ransomNoteFreq.get(i) > magazineFreq.get(i, 0):
                return False
        return True
    
sol = Solution
print(sol.canConstruct("itwqbtcdprfsuprkrjkausiterybzncbmdvkgljxuekizvaivszowqtmrttiihervpncztuoljftlxybpgwnjb", "noclrnthqqganujpsabdjjrwfljribdbwoskcnmtxokkrlvcvsdcxlcqtmugwdedfebnveivovwmkcgncoqslqteecmnekxqkaguebafmmldalfxjexlpiebstahlombvkrpwglbdkbjlmbasdbtrtexubjtepcngbmxujktcipvlwuqvngutrlxkkhjwmsengmdmdesjogpqblacifgtrlaewrcqxtwkrumhusxqmvqlnixrnghtejkrpxmmowunkkbflujojfpcclgdltbcsinuucsjctfxbgcpkbqwpnvghtlgerlatwcsekjhlbswfjxtxkufugaanrblolofhdamiotwqijtqtjcdwgerhkwuufldhrrfiisihpwtsmpqdhnooftgjtcufjejvuepvauemwxkmdaosjdqrcskmrcfmuqagpodjckdwxbgrmqshadaadsxxoawiwfkslxsuovovsmhwbwdtspqdcbddctjkxvwaxhticlgaxbvwjjsfcwojxbhxtlubipditxqtqojphoxxflqgfqlkiqtedhifrlkmqvpnquxdjuxbutlwfupxhahsrbfaajtknlbhixkmnudwojterejauhkqwakihrvccxgasoijeuetmncbsitnfxngqeqvnckvilwsgjtdnorkepwupoluuhrvcgqqthasovrscpbcqautjxjwaxkaapenruqbhficupokqccvgelgqvjgflqxsxonhhqpufsndahsxbauorqbljpvhkmbbhjwdhkdxxwksacjqmkiihbhblccvfqhnptxnfeuktukrwqijdpbmgwokumwxskbgpnjohqtucleruqxfoaodwjxpsdrgslwnhpevhmhnsujijmnrgniehqbhpasbwthrpjpklajovhjjnkkpbgwibfecjdkqnsmdhtdgvgigjuljjliwacbwmosjkuqmwxuraexqlfnfqtpklxmwucrwimbdqkfe"))