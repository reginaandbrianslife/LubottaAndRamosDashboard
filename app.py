doc_choice = st.selectbox("Select Template:", [
    "Notice of Motion: Interim Distribution ($700k)",
    "Affidavit: Executor Fraud & Misconduct",
    "Statement of Claim: Civil Fraud & Removal"
])

if st.button("Generate Legal Draft"):
    st.write("### 📝 Document Preview")
    
    if "Notice of Motion" in doc_choice:
        # (Existing Motion Code)
        pass

    elif "Affidavit" in doc_choice:
        # (Existing Affidavit Code)
        pass

    elif "Statement of Claim" in doc_choice:
        claim_draft = f"""
ONTARIO SUPERIOR COURT OF JUSTICE
BETWEEN: Brian Charles Lubotta (Plaintiff) 
AND: David Michael Lubotta and Maxwell Gotlieb (Defendants)

1. The Plaintiff claims damages for civil fraud and breach of fiduciary duty [cite: 2026-01-04].
2. The Defendants have engaged in a complete breakdown of communication and acted in bad faith [cite: 2026-01-04].
3. The Plaintiff seeks an Order removing the Defendants as executors due to hostility and psychological games [cite: 2026-01-04].
4. An interim distribution of $700,000 is sought to mitigate manufactured financial hardship [cite: 2026-01-04].
        """
        st.code(claim_draft, language="text")
        st.download_button("Download Statement of Claim", claim_draft, "Statement_of_Claim.txt")
