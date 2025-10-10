---
title: Invoice Standardization System INSTAVOICED
kata_name: instavoiced
---

# Invoice Standardization System INSTAVOICED

The system you are building is a cloud-based service called INSTAVOICED. The main customer is a large Swedish enterprise BIGCO. BIGCO wants to streamline their accounts department. Today they receive invoices from around 200 smaller companies in Europe. Each of these suppliers has their own unique way of laying out their invoice information onto a piece of paper. The text will be written in French, German, Italian or Polish. 

Instead of getting paper invoices in the post, BIGCO wants to instead receive all their invoices electronically from INSTAVOICED in a standard xml format (in English). The cloud based INSTAVOICED system will receive the invoices from all the suppliers and forward them to BIGCO in the required format once per day. 

The POST_TO_PDF service is provided by a partner company. They scan paper invoices and upload them to INSTAVOICED in pdf format. Each invoice supplier can either choose to continue to post a paper invoice to the POST_A_PDF service or directly transfer a pdf to INSTAVOICED via their webpage. You estimate about half the suppliers will choose to continue with paper invoices and use the POST_TO_PDF service.

INSTAVOICED converts each pdf invoice into the required standard xml format and forwards it to BIGCO’s internal accounts system. (BIGCO has a secure ftp server where xml files can be written). INSTAVOICED will also take a copy of each pdf invoice and store it in a long-term archive. BIGCO can search for and download old pdf invoices from INSTAVOICED for any given supplier in a given date range.

INSTAVOICED has an onboarding process for BIGCO's suppliers, facilitated by skilled technicians. For each small supplier, a technician creates an OCR mapping from the fields in the original pdf invoice to BIGCO's standard xml fields. This OCR mapping will be used to transform all the invoices from that supplier into xml. 

New suppliers are added and old ones removed at a rate of about 20 per year. The volume of invoices to be handled is about 100 each month, and each xml file is around 500KB. The additional data for each supplier is up to 200KB. Old invoices must be stored for at least 10 years. BIGCO rarely fetches more than 10 old invoices at a time and INSTAVOICED has up to 5 working days to provide them.

