#!/bin/bash
# run_all_tests.sh

echo "🏗️ THE ARCHITECT TEST SUITE 🏗️"
echo "Running complete destruction sequence..."

# Hash all test files
for test in test_*.py; do
    echo "Hashing $test..."
    sha256sum $test >> test_hashes.txt
done

# Run each test
python test_mongodb_complete.py
python test_elasticsearch_complete.py
python test_redis_complete.py
python test_postgresql_complete.py
python test_all_databases.py

echo "Destruction complete."
echo "Check results/ for proof."
echo "Patent #63/841086"
echo "The Architect"