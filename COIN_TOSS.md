# The Coin Toss

A coin toss is commonly represented as a binary event:

1. heads;
2. tails.

The representation serves protocols requiring a binary output. It excludes relations present in the physical system.

A coin can land on its edge. It can roll away, become obstructed, leave the measurement area, be caught, or fail to settle within the observation window. A physical state can occur without producing an admissible measurement. A measurement can occur while the record differs from the measured state.

The protocol often handles these states by declaring the toss invalid and repeating the toss until heads or tails appears. The resulting dataset is binary because the protocol excludes nonbinary results. The binary dataset does not establish that every possible physical outcome is binary.

This exposes four separate layers:

- **physical state:** what happens to the coin;
- **measurement event:** whether the state is distinguished;
- **record:** what the observer or instrument preserves;
- **reported result:** how the record is compressed into an allowed category.

The statement "a coin toss has two possible outcomes" is therefore not a fact about every physical toss. It is a claim produced by a model and enforced by a measurement protocol.

The example demonstrates the Distinction Principle. The categories define what the system can report. It demonstrates Boundary Testing because the edge case reveals where the binary representation stops. It demonstrates Veritas Calculus because the redo rule reveals what the protocol is calculating for: a usable binary result.

It also demonstrates the alignment problem. A classifier forced to choose one of two labels can produce a binary dataset while erasing the third state, unrecorded measurement, and excluded categories. Later systems may train on those outputs and represent the enforced classification as knowledge about reality.

> **A measurement protocol cannot require every event to produce an admissible result.**
