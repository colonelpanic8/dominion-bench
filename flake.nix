{
  description = "Benchmark for Dominion kingdom analysis";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    dominion-engine = {
      url = "github:colonelpanic8/dominion-engine";
      flake = false;
    };
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    dominion-engine,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      packages.default = pkgs.runCommand "dominion-bench" {} ''
        mkdir -p $out/share/dominion-bench
        cp -r ${./cases} $out/share/dominion-bench/cases
        cp -r ${./scripts} $out/share/dominion-bench/scripts
        cp ${./grading.md} $out/share/dominion-bench/grading.md
      '';

      checks.cases = pkgs.runCommand "dominion-bench-cases" {nativeBuildInputs = [pkgs.python3];} ''
        cp -r ${self} src && chmod -R u+w src
        DOMINION_ENGINE=${dominion-engine} python3 -I src/scripts/bench.py check
        touch $out
      '';

      devShells.default = pkgs.mkShell {
        packages = with pkgs; [just alejandra python3];
        DOMINION_ENGINE_PINNED = "${dominion-engine}";
      };

      formatter = pkgs.alejandra;
    });
}
