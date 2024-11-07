export const PATH = "./src/2023/1/";

export function partOne(input: string): number {
  const lines = input.split("\n");

  const values = lines.map((line) => {
    const first = line.split("").find((value) => !isNaN(Number(value)));
    const last = line.split("").findLast((value) => !isNaN(Number(value)));

    if (first && last) return Number(first + last);

    throw Error("Invalid input!");
  });

  return values.reduce((a, b) => a + b);
}

export function partTwo(input: string): number {
  const lines = input.split("\n");

  const digits: Record<string, string> = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
  };

  const values = lines.map((line) => {
    let firstPos: { start: number; end: number } = { start: Infinity, end: 0 };
    let lastPos: { start: number; end: number } = { start: -Infinity, end: 0 };

    Object.keys(digits).forEach((digit) => {
      const firstIndex = line.indexOf(digit);
      const lastIndex = line.lastIndexOf(digit);

      if (firstIndex >= 0 && firstIndex < firstPos.start) {
        firstPos = { start: firstIndex, end: firstIndex + digit.length };
      }

      if (lastIndex >= 0 && lastIndex > lastPos.start) {
        lastPos = { start: lastIndex, end: lastIndex + digit.length };
      }
    });

    if (
      firstPos.start === Infinity ||
      firstPos.end === 0 ||
      lastPos.start === -Infinity ||
      lastPos.end === 0
    ) {
      throw Error("Invalid input!");
    }

    const first = line.slice(firstPos.start, firstPos.end);
    const last = line.slice(lastPos.start, lastPos.end);

    return Number(digits[first] + digits[last]);
  });

  return values.reduce((a, b) => a + b);
}

const input = await Deno.readTextFile(PATH + "input.txt");

console.log("Part One:", partOne(input));
console.log("Part Two:", partTwo(input));
