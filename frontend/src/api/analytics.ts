

export async function fetchAnalyticsSummary() {
  const response = await fetch("http://127.0.0.1:8000/analytics/summary", {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
    },
  });

  if (!response.ok) {
    throw new Error("Failed to fetch analytics");
  }

  return response.json();
}
