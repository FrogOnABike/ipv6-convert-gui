import unittest
from functions import compress_ipv6

class Tests(unittest.TestCase):
    def test_local_address(self):
        address = "0000:0000:0000:0000:0000:0000:0000:0001"
        exp_result = "::1"
        self.assertEqual(
            compress_ipv6(address),
            exp_result,
        )

    def test_iso_address(self):
        address = "fcef:0000:0000:0ab0:7d20:0000:0000:0565"
        exp_result = "fcef::ab0:7d20:0:0:565"
        self.assertEqual(
            compress_ipv6(address),
            exp_result,
        )
    def test_compression_examples(self):
        # Your existing test cases:
        # self.assertEqual(compress_ipv6_address("0000:0000:0000:0000:0000:0000:0000:0001"), "::1")
        # self.assertEqual(compress_ipv6_address("your_random_interview_address_full"), "your_random_interview_address_compressed")

        # New test cases: (6 examples + 1 from your existing set for completeness)
        test_cases = [
            # 1. Longest sequence of zeros in the middle
            ("2001:0db8:0000:0000:0000:ff00:0042:8329", "2001:db8::ff00:42:8329"),
            
            # 2. Zeros at the beginning
            ("0000:0000:0000:0000:1234:5678:9abc:def0", "::1234:5678:9abc:def0"),
            
            # 3. Zeros at the end
            ("fe80:0000:0000:0000:0202:b3ff:fe1e:8329", "fe80::202:b3ff:fe1e:8329"),
            
            # 4. No contiguous zero blocks for '::', only leading zero omission
            ("2001:0db8:85a3:0001:0001:8a2e:0370:7334", "2001:db8:85a3:1:1:8a2e:370:7334"),
            
            # 5. Multiple zero blocks, but only one '::' possible
            ("2001:0db8:0000:1234:0000:0000:5678:0000", "2001:db8:0:1234::5678:0"),
            
            # 6. All zeros (unspecified address)
            ("0000:0000:0000:0000:0000:0000:0000:0000", "::"),
            
            # Your existing local link address (::1)
            ("0000:0000:0000:0000:0000:0000:0000:0001", "::1"),
        ]

        for full_address, expected_compressed in test_cases:
            with self.subTest(full_address=full_address): # subTest helps identify which specific test case failed
                actual_compressed = compress_ipv6(full_address)
                self.assertEqual(actual_compressed, expected_compressed, 
                                    f"Failed for {full_address}: Expected {expected_compressed}, Got {actual_compressed}")

if __name__ == "__main__":
    unittest.main(verbosity=2)