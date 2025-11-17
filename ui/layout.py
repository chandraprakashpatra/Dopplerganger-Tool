import streamlit as st
from core.hashing import hash_folder
from core.grouping import duplicates_inside, duplicates_across
from core.export import export_groups_to_csv, export_cross_to_csv
from core.filecopy import copy_grouped_images, copy_cross

def render():
    st.title("Image Hash Duplicate Finder")

    mode = st.sidebar.selectbox("Mode", ["Single Folder", "Two Folders"])

    if mode == "Single Folder":
        folder = st.text_input("Folder path")
        out_dir = st.text_input("Output folder")

        if st.button("Run"):
            m = hash_folder(folder)
            dup = duplicates_inside(m)
            st.write(f"Groups: {len(dup)}")

            csv_path = export_groups_to_csv(dup, out_dir)
            st.download_button("Download CSV", open(csv_path, "rb"), file_name="duplicates_single.csv")

        if st.button("Copy Images"):
            m = hash_folder(folder)
            dup = duplicates_inside(m)
            copy_grouped_images(dup, out_dir)

    if mode == "Two Folders":
        a = st.text_input("Folder A")
        b = st.text_input("Folder B")
        out_dir = st.text_input("Output folder")

        if st.button("Run"):
            map_a = hash_folder(a)
            map_b = hash_folder(b)
            cross = duplicates_across(map_a, map_b)
            st.write(f"Groups: {len(cross)}")

            csv_path = export_cross_to_csv(cross, out_dir)
            st.download_button("Download CSV", open(csv_path, "rb"), file_name="duplicates_cross.csv")

        if st.button("Copy Images"):
            map_a = hash_folder(a)
            map_b = hash_folder(b)
            cross = duplicates_across(map_a, map_b)
            copy_cross(cross, out_dir)
