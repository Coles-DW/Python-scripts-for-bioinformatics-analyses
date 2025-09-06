from Bio import SeqIO

# Input files with full Windows paths
fasta_file = r"C:\Users\donov\OneDrive\Myrtle rust 2025\Hyperparasite RNA-seq\Extracting protein sequences from fasta\All_Unigene.fa.transdecoder.pep"
gene_id_file = r"C:\Users\donov\OneDrive\Myrtle rust 2025\Hyperparasite RNA-seq\Extracting protein sequences from fasta\genes_of_interest.txt"
output_file = r"C:\Users\donov\OneDrive\Myrtle rust 2025\Hyperparasite RNA-seq\Extracting protein sequences from fasta\matched_proteins.fasta"

# Load gene IDs into a set
with open(gene_id_file) as f:
    gene_ids = set(line.strip() for line in f if line.strip())

# Filter FASTA records that contain any of the gene IDs
matched_records = [
    record for record in SeqIO.parse(fasta_file, "fasta")
    if any(gene_id in record.description for gene_id in gene_ids)
]

# Write matched records to a new FASTA file
SeqIO.write(matched_records, output_file, "fasta")

print(f"Extracted {len(matched_records)} matching sequences to '{output_file}'.")
