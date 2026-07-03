INSERT OR IGNORE INTO users (username, password_hash, name, email, role)
VALUES (
    'admin',
    'scrypt:32768:8:1$tEmJB63JLSXy3oOO$245dbabce999654cadaa4be5eac6874b139377a2ed122ae6f04a9218ebf9861ce60e5773bc5920dcf93d9ee9e24e531c458fa19e39da38224df49e30249583a9', 
    'System Admin',
    'admin@crm.local',
    'admin'   
); 
INSERT OR IGNORE INTO interns (
    first_name, last_name, email, phone, school, department,
    internship_start, internship_end, status
)
VALUES (
    'Ahmet', 'Yılmaz', 'ahmet@example.com', '05551234567',
    'Pamukkale Üniversitesi', 'Yönetim Bilişim Sistemleri',
    '2026-07-01', '2026-08-31', 'active'
);

INSERT OR IGNORE INTO intern_notes (intern_id, admin_id, note)
VALUES (1, 1, 'İlk görüşme yapıldı.');

INSERT OR IGNORE INTO intern_documents (intern_id, file_name, file_type)
VALUES (1, 'staj_sozlesmesi.pdf', 'application/pdf'); 

