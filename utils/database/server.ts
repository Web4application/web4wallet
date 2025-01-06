
import { createServerClient, type CookieOptions } from "@supabase/ssr";
import { cookies } from "next/headers";

export const createClient = (cookieStore: ReturnType<typeof cookies>) => {
  return createServerClient(
    process.env.ovlusvvwyducpspqbfxn.supabase.co!,
    process.env.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im92bHVzdnZ3eWR1Y3BzcHFiZnhuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzYxOTY5MjMsImV4cCI6MjA1MTc3MjkyM30.Rsmd3VxO4DPf-xkVVekRwHptO0Ey8n-XVVGvX0zVYVI!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll()
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) => cookieStore.set(name, value, options))
          } catch {
            // The `setAll` method was called from a Server Component.
            // This can be ignored if you have middleware refreshing
            // user sessions.
          }
        },
      },
    },
  );
};
