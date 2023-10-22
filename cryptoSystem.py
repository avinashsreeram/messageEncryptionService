import random
# from retrying import retry


# @retry(stop_max_attempt_number=5, wait_fixed=10000)
def decrypt(receivedMessage):
    try:
        keyList = []
        decryptedMessage = ""
        while 27 < receivedMessage:
            quotient = receivedMessage // 27
            reminder = receivedMessage % 27
            keyList.append(reminder)
            receivedMessage = quotient
        keyList.append(receivedMessage)
        keyList.reverse()
        for value in keyList:
            if value == 0:
                decryptedMessage += " "
            else:
                decryptedMessage += (chr(value + 64))
        return decryptedMessage
    except Exception as e:
        print("Exception in decrypt: ", e)
        raise e


# @retry(stop_max_attempt_number=5, wait_fixed=10000)
def computePrivateKey(publicKey, phiOfN):
    try:
        gcd, s, t = euclidianGcd(publicKey, phiOfN)
        privateKey = s + phiOfN
        return privateKey
    except Exception as e:
        print("Exception in computePrivateKey: ", e)
        raise e


# @retry(stop_max_attempt_number=5, wait_fixed=10000)
def generateBearCatII(message):
    try:
        bearCatII = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26,
            " ": 27
        }
        sumValue = 0
        for index, character in enumerate(message):
            sumValue += bearCatII[character] * 27 ** (len(message) - index - 1)
        return sumValue
    except Exception as e:
        print("Exception in generateBearCatII: ", e)
        raise e


# @retry(stop_max_attempt_number=5, wait_fixed=10000)
def euclidianGcd(a, b):
    try:
        if b == 0:
            return a, 1, 0
        else:
            r = a % b
            q = a // b
            g, s, t = euclidianGcd(b, r)
            s_t = s
            s = t
            t = s_t - t * q
            return g, s, t
    except Exception as e:
        print(" Exception in euclidianGcd: ", e)
        raise e


# @retry(stop_max_attempt_number=5, wait_fixed=10000)
def millerRabinTest(num, k):
    try:
        # k is the number of iterations (parameter) which affects the accuracy
        #  of the test. use can use either
        if num <= 1 or num == 4:
            return False
        if num <= 3:
            return True
        while k > 0:
            random_a = 2 + (random.randrange(2, num - 2) % (num - 4))
            if pow(random_a, num - 1, num) != 1:
                return False
            k = k - 1
        return True
    except Exception as e:
        print("Exception in millerRabinTest", e)
        raise e


# @retry(stop_max_attempt_number=5, wait_fixed=10000)
def generatePrimeNumbers():
    try:
        universalTrue = True
        # k is the number of iterations (parameter) which affects the
        # accuracy of the test. use can use either
        # k as 3 or 5 etc.
        p = 0
        q = 0

        k = 3
        while universalTrue:
            p = random.randrange(1000000000000000, 5000000000000000)
            q = random.randrange(1000000000000000, 5000000000000000)
            if millerRabinTest(p, k) and millerRabinTest(q, k):
                return p, q
    except Exception as e:
        print("Exception in generatePrimeNumbers: ", e)
        raise e


def triggerCryptoSystem():
    try:
        print("RSA Crypto System Activated: ")
        universalTrue = True
        # where p and q are two prime numbers whose product value is 
        # equal to n i.e. (n=p*q)
        p, q = generatePrimeNumbers()
        n = p * q
        phiOfN = (p - 1) * (q - 1)
        publicKey = 0
        while universalTrue:
            publicKey = int(input("Please enter the Public Key Information: "))
            gcd, s, t = euclidianGcd(publicKey, phiOfN)
            if gcd == 1:
                break
        inputMessage = input("Please enter you message below: ").upper()
        print("Entered Value: ", inputMessage)
        messageInBearcatII = generateBearCatII(inputMessage)
        encryptedMessage = pow(messageInBearcatII, publicKey, n)
        privateKey = computePrivateKey(publicKey, phiOfN)
        receivedMessage = pow(encryptedMessage, privateKey, n)
        plainTextMessage = decrypt(receivedMessage)
        print("p: ", p)
        print("q: ", q)
        print("n: ", n)
        print("M: ", inputMessage)
        print("C/encrypted Message: ", encryptedMessage)
        print("P: ", plainTextMessage)
    except Exception as e:
        print("Exception occurred in main function: ", e)
        raise e


if __name__ == "__main__":
    triggerCryptoSystem()
