class Solution:

    def swapShipmentOrder(self, shipmentOrder, windowSize):
        result = []

        for i in range(len(shipmentOrder) - windowSize + 1):
            result.append(
                shipmentOrder[:i]
                + sorted(shipmentOrder[i : i + windowSize])
                + shipmentOrder[i + windowSize :]
            )


        result.sort(reverse=True)
        return result[0]


if __name__ == "__main__":
    windowSize = int(input("Enter the window size: "))
    shipmentOrder = list(
        map(int, input("Enter shipment order values separated by spaces: ").split())
    )
    print(Solution().swapShipmentOrder(shipmentOrder, windowSize))