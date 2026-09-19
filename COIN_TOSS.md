# The Coin Toss

A coin toss is commonly represented as a binary event:

1. heads;
2. tails.

This representation serves protocols requiring a binary output. It does not establish that the represented categories exhaust every possible physical state.

A coin can land on its edge. It can roll away, become obstructed, leave the measurement area, be caught, or fail to settle within the observation window.

A physical state can occur without producing an admissible protocol result. A measurement can occur while the retained record differs from the measured state. A record can also be transformed into a reported category that contains less information than the state or measurement from which it was produced.

The protocol commonly handles excluded states by declaring the toss invalid and repeating it until heads or tails appears.

The resulting dataset is binary because the protocol retains heads and tails as admissible results.

That does not establish that every possible physical outcome is binary.

## Represented layers

The example exposes at least four distinguishable layers:

- **physical state:** what happens to the coin;
- **measurement event:** what distinction is performed on that state;
- **record:** what the observer or instrument retains from the measurement;
- **reported result:** how the retained record is represented within the protocol's permitted categories.

These layers can correspond closely without being identical.

The transformation can be represented as:

```text
physical state
→ measurement
→ record
→ reported result
