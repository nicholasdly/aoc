import { assertEquals } from "jsr:@std/assert@1";
import { partOne, partTwo, PATH } from "./solution.ts";

Deno.test("part one solution correctly solves example", async () => {
  const input = await Deno.readTextFile(PATH + "example1.txt");

  const actual = partOne(input);
  const expected = 142;

  assertEquals(actual, expected);
});

Deno.test("part two solution correctly solves example", async () => {
  const input = await Deno.readTextFile(PATH + "example2.txt");

  const actual = partTwo(input);
  const expected = 281;

  assertEquals(actual, expected);
});
